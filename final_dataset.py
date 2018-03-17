import sys
import os
import re
import glob
from pprint import pprint
#csv = open("final_dataset.csv", "w")

#d1=630
#d2=634
#d3=719
#d4=780

#file = "12275.txt" 
#file2="/home/sagarwal/Blockchain/train_delay/train_12275.txt"


#file = "12417.txt" 
#file2="/home/sagarwal/Blockchain/train_delay/train_12417.txt"



#file = "14511.txt" 
#file2="/home/sagarwal/Blockchain/train_delay/train_14511.txt"



file = "12404.txt" 
file2="/home/sagarwal/Blockchain/train_delay/train_12404.txt"



csv = open("final_dataset.csv", "a+") 

cnt=0
en=8
cnt2=0
with open(file) as fi:
    lines = [line for line in fi]
with open(file2) as fi:
    cal_delay = [line for line in fi]
while True:
    line=lines[cnt:en]
    if len(line)==0:
        break
    cnt=cnt+8
    en=en+8
    #pprint (rt)
    par=0
    p1=[]
    p2=[]
    p3=[]
    p=[]
    for i in line:
        arr=i.split(",")
        p.append(arr[1])

        p1.append(arr[3])
        p2.append(arr[4])
        p3.append(arr[5])
        par=par+1
    result=''
    res2=''
    res3=''
    for i in range(0,8):
        result+=p1[i]+','
        res2+=p2[i]+','
        res3+=p3[i]+','


    a2 = p[0].split('-')
    st = ''
    st = a2[0]+','+a2[1]+','+a2[2]

    for cal in cal_delay:
        if st in cal:
            csv.write(result+'\n')
            csv.write(res2+'\n')
            csv.write(res3+'\n')
            csv.write('780\n')
            csv.write(cal.split(',')[3])
            
            break

       
        