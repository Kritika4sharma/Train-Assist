#for train 12404
import os
import sys
import requests
from datetime import date, timedelta
from pprint import pprint 
d1 = date(2017,1,1)  # start date
d2 = date(2017, 12, 31)  # end date

delta = d2 - d1  
city=[]
'''
city.append('Jaipur')
city.append('Alwar')
city.append('Mathura')
city.append('Agra')
city.append('Tundla')
city.append('Kanpur')
city.append('Fatehpur')
city.append('Allahabad')

file='weather_city.csv'
f= open('12404.txt',"a+")
sys.stdout=f
for i in range(delta.days + 1):
    pres_data = d1 + timedelta(days=i)
    for c in city:
        with open(file) as fi:
            for line in fi: 
                if str(pres_data) in line:
                    if c in line:
                        print line,
'''

city.append('Allahabad')
city.append('Fatehpur')
city.append('Kanpur')
city.append('Aligarh')
city.append('Delhi')

file='weather_city.csv'
f= open('12417.txt',"a+")
sys.stdout=f
for i in range(delta.days + 1):
    pres_data = d1 + timedelta(days=i)
    for c in city:
        with open(file) as fi:
            for line in fi: 
                if str(pres_data) in line:
                    if c in line:
                        print line,


'''

city.append('Allahabad')
city.append('Lucknow')
city.append('Bareilly')
city.append('Moradabad')
city.append('Meerut')

file='weather_city.csv'
f= open('14511.txt',"a+")
sys.stdout=f
for i in range(delta.days + 1):
    pres_data = d1 + timedelta(days=i)
    for c in city:
        with open(file) as fi:
            for line in fi: 
                if str(pres_data) in line:
                    if c in line:
                        print line,

'''
'''
city.append('Allahabad')
city.append('Fatehpur')
city.append('Kanpur')
city.append('Aligarh')
city.append('Delhi')

file='weather_city.csv'
f= open('12275.txt',"a+")
sys.stdout=f
for i in range(delta.days + 1):
    pres_data = d1 + timedelta(days=i)
    for c in city:
        with open(file) as fi:
            for line in fi: 
                if str(pres_data) in line:
                    if c in line:
                        print line,

'''