""" 
Data analysis tool for Robot AAC project

Author: Younghyun Chung
Date: 14th June, 2013


""" 

import csv as csv

filename = "../data/RobotAAC-0430.txt"

lines = list(csv.reader(open(filename, 'rb'), delimiter='|'))

for line in lines:
  print(line)
"""
with open("../data/RobotAAC-0430.txt") as f:
  c = csv.reader(f, delimiter='|')
  for line in c:
    print(line)



open_file_object_temp = csv.writer(open("../result/myfirstforest_temp.csv", "wb"))
i = 0
for row in train_data:
  if 'Mr.'        in train_data[i, 2]: title = 1
  elif 'Mrs.'     in train_data[i, 2]: title = 2
  elif 'Miss.'    in train_data[i, 2]: title = 3
  elif 'Master.'  in train_data[i, 2]: title = 4
  else: title = 0


open_file_object = csv.writer(open("../result/myfirstforest_.csv", "wb"))
test_file_object = csv.reader(open('../data/test.csv', 'rb')) #Load in the csv file

test_file_object.next()
i = 0
for row in test_file_object:
    row.insert(0,output[i].astype(np.uint8))
    open_file_object.writerow(row)
    i += 1
 """