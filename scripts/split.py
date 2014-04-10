#!/usr/bin/python

from datetime import date

year = 2013
split_date = date(year, 07, 15)
begin_date = date(year, 04, 15)
date_delta_std = (split_date - begin_date).days

fin = open("input/input.csv")
train = open("output/train.csv", "w")
test = open("output/test.csv", "w")

fin.readline()
for line in fin.readlines():
    line = line.strip()
    entrys = line.split(",")
    entrys_date = date(year, int(entrys[3]), int(entrys[4]))
    date_delta = (entrys_date - begin_date).days
    if date_delta < date_delta_std:
        train.write(",".join(entrys[:3]) + "," + str(date_delta) + "\n")
    elif 1 == int(entrys[2]):
        test.write(",".join(entrys[:2]) + "\n")

test.write("999999999,-1" + "\n")

test.close()
train.close()
fin.close()
