import sys
import os
import re

filename = raw_input()
out_file = filename[:-4]+"_out.csv"
csv = open(out_file, "w") 

with open("data.txt") as fi:   
	result = ""
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
			result = ""


