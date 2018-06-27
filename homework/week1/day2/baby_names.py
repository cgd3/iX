# -*- coding: utf-8 -*-
"""
In this example we are going to build an application that reads the most popular names
in the US, taken from the Social Security Administration's site:

https://www.ssa.gov/oact/babynames/

This application will have the following functionalities:

- It will accept a name as an argument
- It will read a list of files (located in the folder data). Each file contains the
most popular baby names for boys and girls for a certain year (the year is in the filename)
- For the name provided as an argument, print out how many years it's been among the most popular among boys and girls
"""

##need to create file with first line of each txt file 

from collections import Counter 

def load_names():
       
    boy_names = []
    girl_names = []
    
    #read in data 
    years = range(1900, 2017)
    for i in years:
        with open('data/names_{}.txt'.format(i)) as f:
            first_line = f.readline().strip('\n')
            
            boy_names.append((first_line.split('|')[1]))
            girl_names.append((first_line.split('|')[2]))
            #print(boy_names)
            #print(girl_names)
   
    #create dictionaries to count names 
    boy_dictionary = Counter(boy_names)
    girl_dictionary =Counter(girl_names)
    print(boy_dictionary)
    print(girl_dictionary)
    
    #accept name as argument 
    name_input = input("Insert your name").capitalize()
    
    if name_input not in (girl_dictionary and boy_dictionary):
        print("This name was most popular 0 times for boys and girls")
    elif name_input in girl_dictionary:
        print("This name was most popular {} time for girls and 0 times for boys".format(girl_dictionary[name_input]))
    elif name_input in boy_dictionary:
        print("This name was most popular 0 time for girls and {} times for boys".format(boy_dictionary[name_input]))
    

load_names()
            
            