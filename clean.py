""" 
Data analysis tool for Robot AAC project

Author: Younghyun Chung
Date: 14th June, 2013


""" 

import csv
import time

in_file = "../data/RobotAAC-0430.txt"
out_file = "../result/RobotAAC-0430.csv"

rows = list(csv.reader(open(in_file, 'rb'), delimiter='|', skipinitialspace=True))

data=[]
data.append(["timestamp", "id", "command", "adjusted_timestamp", "datetime", "elapsed_time"]) 

last_time = int(rows[0][0])

for line in rows:
#  if line[2] and not line[2] == "Keep Alive":
  if line[2]:
    if line[1] == '0':
      line.append(int(line[0])+3)
    elif line[1] == '1': 
      line.append(int(line[0]))
    elif line[1] == '2': 
      line.append(int(line[0])-1)
    elif line[1] == '3': 
      line.append(int(line[0])+1)
    elif line[1] == '4': 
      line.append(int(line[0])-180)
    else:
      line.append(int(line[0]))

    line.append(time.strftime('%Y-%m-%d %H:%M:%S', \
                time.localtime(int(line[3])))) # timestamp

    line.append(int(line[3]) - last_time) # elapsed_time
    last_time = int(line[3])              # update new last_time


    data.append(line)
    print(line)

open_file_object = csv.writer(open(out_file, "wb"))

for row in data:
  open_file_object.writerow(row)

