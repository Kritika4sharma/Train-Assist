import os
import sys
import requests
from datetime import date, timedelta
from pprint import pprint 
from numpy import random
import json
import pickle
import scipy
import datetime

train_num=input('train_num ')
predict_date=input('date_for_prediction ')
present_date=datetime.datetime.strftime(datetime.datetime.now() - timedelta(4), '%Y-%m-%d')

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

URL='https://api.railwayapi.com/v2/route/train/'+train_num+'/apikey/l8zz053ekd/'
r = requests.get(url = URL,verify=True)
data = r.json()

filePathNameWExt =  'data.json'
with open(filePathNameWExt, 'w+') as fp:
    json.dump(data, fp)

data = json.load(open('data.json'))
temp = data['route']

name_of_train = data['train']['name']

distance=0
lat=[]
lon=[]
length = len(temp)
lat.append(temp[0]['station']['lat'])
lon.append(temp[0]['station']['lng'])

tot_num=(length-2)/3
for i in range(0,3):
    index=int((tot_num)*(i+1))
    lat.append(temp[index]['station']['lat'])
    lon.append(temp[index]['station']['lng'])
    
lat.append(temp[length-1]['station']['lat'])
lon.append(temp[length-1]['station']['lng'])

distance=temp[length-1]['distance']

key="77ba2051b6623b323386dd146cfa852f"
p1=[]
p2=[]
p3=[]
for cnt in range(0,5):
    URL="https://api.darksky.net/forecast/" + key +"/"+str(lat[cnt])+',%20'+str(lon[cnt])+','+str(predict_date)+"T00:00:00?exclude=currently%2Cminutely%2Chourly%2Calerts%2Cflags"
    URL2="https://api.darksky.net/forecast/" + key +"/"+str(lat[cnt])+',%20'+str(lon[cnt])+','+str(present_date)+"T00:00:00?exclude=currently%2Cminutely%2Chourly%2Calerts%2Cflags"
    r = requests.get(url = URL,verify=True)
    data = r.json()
    r2 = requests.get(url = URL2,verify=True)
    data2 = r2.json()

    filePathNameWExt = "predicted_weather.json"
    with open(filePathNameWExt, 'w+') as fp:
        json.dump(data, fp)
    data = json.load(open(filePathNameWExt))

    filePathNameWExt2 = "present_weather.json"
    with open(filePathNameWExt2, 'w+') as fp2:
        json.dump(data2, fp2)
    data2 = json.load(open(filePathNameWExt2))

    if(present_date >= predict_date):
        p1.append(data['daily']['data'][0]['visibility'])
        #print("past day")
    else:
        p1.append(data2['daily']['data'][0]['visibility'])
        #print("future day")
    p2.append (data['daily']['data'][0]['temperatureMax'])
    p3.append (data['daily']['data'][0]['temperatureMin'])

result = []
for i in range(0,5):
    result.append(p1[i])

for i in range(0,5):
    result.append(p2[i])

for i in range(0,5):
    result.append(p3[i])

result.append(distance)

if 'Shatabdi' in name_of_train:
    type_t=0
elif 'Duronto' in name_of_train:
    type_t=0
elif 'Rajdhani' in name_of_train:
    type_t=0
else:
    type_t=1

result.append(type_t)

print(loaded_model.predict([result]))




'''
correct prediction
	train_num 14512
	present_date 2017-08-01
    right time
'''