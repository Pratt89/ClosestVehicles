# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:54:55 2021

@author: PraTiK ChavhaN aLias </steve_Rogers>
"""
import os
print(os.listdir())

from DatabaseCreation import DatabaseCreation

def FetchCabs(x, y):
    filename = 'cabs.json'
    list_of_closest_cabs = []
    # creating database cabs.json
    database = DatabaseCreation(filename)
    database.create_database()
    # insert 100 random data
    database.insert_100_random_data_entries_into_database()
    # insert next 99900 random data
    database.insert_100k_random_data_entries_into_database()
    # getting data from cabs.json(database)
    data = database.get_data()
    
    list_of_cabs = []
    # if database not present
    if(data == "Databse "+filename+" does not exist"):
        pass
    # calculate distance
    else:
        d=0
        for k in data.keys():
            x1 = data[k]['x']
            y1 = data[k]['y']
            list_of_cabs += [[x1, y1]]
            # list_of_cabs.sort()
            d = ((x1-x)**2 + (y1-y)**2)**0.5
            # if(i==1):
            #     d = ((x1-x)**2 + (y1-y)**2)**0.5
            # else:
            #     temp = ((x1-x)**2 + (y1-y)**2)**0.5
            #     if(temp<d):
            #         d = temp
            list_of_cabs[-1].insert(0, d)
        list_of_cabs.sort()
        list_of_closest_cabs = list_of_cabs[:5]
        
        for i in range(5):
            d = list_of_closest_cabs[i].pop(0)
            # print(d)
            
    return list_of_closest_cabs

if __name__ == '__main__':
    x, y =  list(map(int, input().split()))
    
    # getting list of top 5 cabs closest to the user
    list_of_closest_cabs = FetchCabs(x, y)
    print("Closest vehicles : ", *list_of_closest_cabs)