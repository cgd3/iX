# -*- coding: utf-8 -*-
import scrapy


class BookscrapSpider(scrapy.Spider):
    name = 'bookscrap'
    allowed_domains = ['http://books.toscrape.com/']
    start_urls = ['http://http://books.toscrape.com//']

    def parse(self, response):
        category_urls = [response.urljoin(url) for url in response.css("ul.nav-list>li>ul>li>a::attr(href)").extract()]
        for url in category_urls:
            yield scrapy.Request(url, callback=self.parse_category)

    def parse_category(self, response):
        book_urls = [response.urljoin(href) for href in response.css("article h3 a::attr(href)").extract()]
        next_href = response.css("li.next>a::attr(href)").extract_first()
        for url in book_urls:
            yield scrapy.Request(url, callback=self.parse_book)
        if next_href:
            next_url = response.urljoin(next_href)
            yield scrapy.Request(next_url, callback=self.parse_category)

    def parse_book(self, response):
        table_keys = response.css("table th::text").extract()
        table_values = response.css("table td::text").extract()
        data = dict(zip(table_keys, table_values))

        main = response.css("div.product_main")
        title = main.css("h1::text").extract_first()
        rating = main.css("p.star-rating::attr(class)").extract_first().replace("star-rating", "").strip()
        category = response.css("ul.breadcrumb>li>a::text").extract()[-1]
        description = response.css("div#product_description+p::text").extract_first()

        data["description"] = description
        data["category"] = category
        data["title"] = title
        data["rating"] = rating
        yield data
