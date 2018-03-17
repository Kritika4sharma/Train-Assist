'''
# importing the requests library
import requests
from pprint import pprint 

# api-endpoint
URL = "https://api.darksky.net/forecast/d0018e9dc336a93402173ddfafbb4743/25.4358,%2081.8463,2017-03-16T00:00:00?exclude=currently%2Cminutely%2Chourly%2Calerts%2Cflags"
 
# sending get request and saving the response as response object
r = requests.get(url = URL)
 
# extracting data in json format
data = r.json()
 
pprint (data)

'''
import os
import sys
import requests
from datetime import date, timedelta
from pprint import pprint 
d1 = date(2017,5,9)  # start date
d2 = date(2017, 12, 31)  # end date

delta = d2 - d1         # timedelta
cities=[]
lat=[]
lon=[]
cities.append('Kanpur'),lat.append('26.4499'),lon.append('80.3319')


key='69f73a7383a2fde5d2f9713e1671c585'

pre_out=sys.stdout
cnt=0
for city in cities:
    print(city)
    os.chdir('/home/sagarwal/Blockchain/dataset')
    f= open(city+'.txt',"a+")
    sys.stdout=f
    for i in range(delta.days + 1):
        pres_data = d1 + timedelta(days=i)
        print(pres_data)
        #print cnt
        URL="https://api.darksky.net/forecast/" + key +"/"+lat[cnt]+',%20'+lon[cnt]+','+str(pres_data)+"T00:00:00?exclude=currently%2Cminutely%2Chourly%2Calerts%2Cflags"
        r = requests.get(url = URL,verify=True)
        data = r.json()
        pprint(data)
    sys.stdout=pre_out
    cnt=cnt+1