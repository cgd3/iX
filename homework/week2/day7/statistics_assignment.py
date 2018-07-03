# -*- coding: utf-8 -*-
"""
Statistics Assignment: Apartment Search tool

This assignment will help us solidify what we have learned so far about data 
manipulation and statistics

Using the Airbnb dataset (located in data/airbnb.csv), we are going to make a script
with the following functionalities:
*******************************************************************************
Functionality 1: Neighbourhood information
- Given a neighbourhood, the tool will provide the following information to the user
  - Total number of available listings in the neighbourhood
  - Number of rooms broken down per listing type
  - Average Room Price
  - Price quartiles

For example if we run the script like;

"python statistics_assignment.py information Belém"

The script will print out information about Belem.

*******************************************************************************
Functionality 2: Apartment Search.
This functionality will help the user to find an appropriate listing. It will ask
the user different listing requirements:
- desired price range
- desired number of rooms (a range)
- a list of desired neighbourhoods
If the user doesnt specifiy any of the requirements (pressing enter without typing anything)
We will consider that the user is indiferent

It will also ask the user if he/she prefers the results sorted by price, by average score
or by number of reviews.

Finally the script will print out the top 10 results matching the desired requirements and sorted
by the desired sorting criteria.

If there are no listings that match the criteria, the script will tell the user that no
listings match the criteria.

For example if we run

"python statistics_assignment.py search"

The script will start prompting us for the requirements and finally print out the results
*******************************************************************************

There should be a main() function that serves as an entrypoint.

When we load the script it will load the dataset and it will be used as the data source.
"""
import sys
import pandas as pd

Arg1 = sys.argv[1]
neighborhood = sys.argv[2]
data = pd.read_csv("airbnb.csv")
df = pd.DataFrame(data)

def information(neighborhood):
    """ functionality 1"""
    neighborhood_data = data[data.neighborhood == neighborhood]
    #Total number of available listings in the neighbourhood
    total_listings = len(neighborhood_data)
    #Number of rooms broken down per listing type
    num_rooms = neighborhood_data.groupby("room_type").bedrooms.count()
    #Average Room Price
    avg_price = neighborhood_data.price.mean()
    #Price quartiles
    price_quartiles = [neighborhood_data.price.quantile(.25), neighborhood_data.price.quantile(.50), neighborhood_data.price.quantile(.75)]
    
    print("Total Listings: " + str(total_listings))
    print("Rooms per listing type: " + str(num_rooms))
    print("Average Price: " + str(avg_price))
    print("Price Quartiles: " + str(price_quartiles))
    

def search(neighborhood):
    """ functionality 2"""
    pass

def parse_arguments():
    """ parses the arguments"""
    pass

def main(Arg1):
    """main entrypoint"""
    if(Arg1 == "information"):
        information(neighborhood)
    else: 
        search(neighborhood)
        
main(Arg1)


#if __name__ == "__main__":
    #arguments = parse_arguments()
    #main(arguments)
