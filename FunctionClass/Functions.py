'''
Name: Aria Nielsen
email: nielseai@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that use APIs to create dictionaries and extract data.
'''

def iterate_dictionary(myDictionary):
    for k, v in myDictionary.items():
        print ("key is " + str(type(k)) + ", value is " + str(type(v)))
        if isinstance(v, dict):
            iterate_dictionary(v)
        else:
            print("{0} : {1}".format(k, v))
            if (isinstance(v, list)):
                for vv in v:
                    if (isinstance(vv, dict)):
                        iterate_dictionary(vv)
                        
def iterate_dictionary2(myDictionary):
        for k, v in myDictionary.items():    
            print("{0} : {1}".format(k, v))
            if (isinstance(v, list)):
                for vv in v:
                    if (isinstance(vv, dict)):
                        iterate_dictionary(vv)
def iterate_dictionary3(myDictionary):
    for k, v in myDictionary.items():
        print ("key is " + str(type(k)) + ", value is " + str(type(v)))
        
                        