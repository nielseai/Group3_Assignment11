'''
Name: Aria Nielsen
email: nielseai@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that use APIs to create dictionaries and extract data.
'''
# Main.py
import json
import requests
from FunctionClass.Functions import *

response = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=slbe&api_key=0clFHEvPAZVcKAwIqcyGQIHuFK4nAqfwJDDjK4ut')
json_string = response.content
    
sleeping_bear = json.loads(json_string) # Turning sleeping bear dunes data into a python dictionary here
    
    
#for park in sleeping_bear['data']:        # Get the value associated with sleeping_bear['data']
    #print (park)
    

#iterate_dictionary(sleeping_bear)
#list1 = [iterate_dictionary(sleeping_bear)]

#print(list1)
print('Here are the directions:')
print(sleeping_bear['data'][0]['directionsInfo']) # retrieving directions data from dictionary
print('Here is the description:')
print(sleeping_bear['data'][0]['description']) # retrieving description data from dictionary
print('Here are the entrance Fees:')
print(sleeping_bear['data'][0]['entranceFees']) # retrieving entrance fees data from dictionary
