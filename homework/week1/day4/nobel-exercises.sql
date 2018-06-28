-- SQL Exercises
-- --------------------
-- Use the nobel database from class to answer the following questions.

-- 1. Select the nobel database.

USE nobel;

-- 2. List the tables.

SHOW tables;

-- 3. Select the first ten records from the laureate table.

SELECT * 
FROM laureate
LIMIT 10;

-- 4. Find the birth and death dates for Albert Einstein.

SELECT name, birth_date, death_date
FROM laureate
WHERE name = 'Albert Einstein';

-- 5. Find the Nobel Laureates who died in 2015 and whose name begins with 'Y'.

SELECT *
FROM laureate
WHERE name like 'Y%' AND death_date like '2015%';

-- 6. Find the last three Nobel Laureates born in 1900.

SELECT * 
FROM laureate
WHERE birth_date LIKE '1900%'
ORDER BY birth_date DESC
LIMIT 3;


-- 7. Find the number of Nobel Prizes awarded between 1950 and 1960.

SELECT COUNT(*)
FROM prize
WHERE (year >= 1950) AND (year <= 1960);

-- 8. Find the number of Nobel Prizes awarded in each year.

SELECT year, COUNT(*) as total
FROM prize
GROUP BY year;

-- 9. In which year was the greatest number of Nobel Prizes awarded?

SELECT year, COUNT(*) as total
FROM prize
GROUP BY year
ORDER BY total DESC
LIMIT 1;

-- 10. What is the average number of Nobel Prizes awarded per year? Do we know how to do this yet?

##see 16 - same question. 
		
-- 11. In which years were more than fifteen Nobel Prizes awarded?

SELECT year, COUNT(*) as total
FROM prize
GROUP BY year 
HAVING total > 15;

-- 12. Who is the Nobel Laureate with the shortest name?

SELECT name
FROM laureate
WHERE length(name) = (SELECT MIN(LENGTH(name)) FROM laureate);

-- 13. Which Nobel Laureate had the longest life? You might need to use IFNULL().

SELECT name, death_date, birth_date, DATEDIFF(death_date, birth_date) as AGE
FROM laureate
WHERE death_date IS NOT NULL
GROUP BY age DESC
LIMIT 1;

-- 14. Which year has the most women Nobel Laureates?

SELECT year, COUNT(*) as women
FROM prize
INNER JOIN laureate
ON prize.laureate_id = laureate.id
WHERE sex = 'F'
GROUP BY year
ORDER by women DESC
LIMIT 1;

-- 15. Which category has the most women Nobel Laureates?

SELECT category, COUNT(*) as women
FROM prize
INNER JOIN laureate
ON prize.laureate_id = laureate.id
WHERE sex = 'F'
group BY category
ORDER BY women DESC
LIMIT 1;

-- 16. What is the average number of Nobel Prizes awarded per year?

SELECT AVG(total)
FROM(
	SELECT year, COUNT(*) as total FROM prize GROUP BY year
	) AS average;
	