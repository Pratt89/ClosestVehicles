# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:38:27 2021

@author: PraTiK ChavhaN aLias </steve_Rogers>
"""
import random
import json
import os

class DatabaseCreation:
    def __init__(self, filename):
        self.filename = filename
        
    def create_database(self):
        if(self.filename not in os.listdir()):
            # Creates a new file
            with open(self.filename, 'w') as fp:
                pass
            
        else:
            return "Database "+self.filename+" already exists"   
    
    def insert_100_random_data_entries_into_database(self):
        vehicleid = 0
        data = dict()
        # if file is present in directory
        if(self.filename in os.listdir()):                
            for i in range(100):
                vehicleid += 1
                x = round(random.uniform(0, 1000), 2)
                y = round(random.uniform(0, 1000), 2)
                obj = {
                    'x' : x,
                    'y' : y
                    }
                data[vehicleid] = obj
                # print(data)

            # creating json object
            data = json.dumps(data, indent=4)
            print('1', type(data))
                        
            # open database
            with open(self.filename, 'w') as fp:
                fp.write(data)
                
        else:
            return "Databse "+self.filename+" does not exist"                      
    
    def insert_100k_random_data_entries_into_database(self):
        vehicleid = 100
        # if file is present in directory
        if(self.filename in os.listdir()):  
            # Opening json file
            with open(self.filename, 'r') as fp:
                # Reading from json file
                data = json.load(fp)
            print('2', type(data))
            data = dict(data)
            
            # 100k - first 100 entries = 99900           
            for i in range(99900):
                vehicleid += 1
                x = round(random.uniform(0, 1000), 2)
                y = round(random.uniform(0, 1000), 2)
                # creating json object
                obj = {
                    'x' : x,
                    'y' : y
                    }
                data[vehicleid] = obj
            print('6', type(data))

            # creating json object
            data = json.dumps(data, indent=4)
            print('3', type(data))
            
            # open database
            with open(self.filename, 'w') as fp:
                fp.write(data)
                
        else:
            return "Databse "+self.filename+" does not exist" 
    
    def get_data(self):
        # if file is present in directory
        if(self.filename in os.listdir()):  
            # Opening json file
            with open(self.filename, 'r') as fp:
                # Reading from json file
                data = json.load(fp)
            print('4', type(data))
            data = dict(data) 
            print('5', type(data))
            return data
            
        else:
            return "Databse "+self.filename+" does not exist" 
            
                            