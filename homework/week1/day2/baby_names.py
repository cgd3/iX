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
n = 2017 - 1900
for i in range(n):
    #print(names_{}.format())

#with open('data/names_1900.txt') as f:
#    first_line = f.readline()
#    print(first_line)