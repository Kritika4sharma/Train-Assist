import sys
import os
import re
import glob

csv = open("out.csv", "w") 
for file in sorted(glob.glob("/home/sagarwal/Blockchain/dataset/*")):
	filename = file
	print filename
	with open(file) as fi:
		temp = filename.split('/')
		temp = temp[len(temp)-1][:-4]
		result = temp+','
		for line in fi:         
			if("2017" in line):
				result += line.strip() + ","
			if("visibility" in line):
				result += line.split(":")[1].split(',')[0].strip()
				result += ","  
			elif("precipType" in line):
				result += line.split(":")[1].split(',')[0].strip()[2:-1]
				result += ","
			elif("temperatureMax" in line):
				if "temperatureMaxTime" not in line:
					result += line.split(":")[1].split(',')[0].strip()
					result += ","
			elif("temperatureMin" in line):
				if "temperatureMinTime" not in line:
					result += line.split(":")[1].split(',')[0].strip()
					result += ","
			elif("windSpeed" in line):
				result += line.split(":")[1].split(',')[0].split('}]}')[0].strip()
			elif("latitude" in line):
				result += "\n"
				csv.write(result)
				result = temp+','
