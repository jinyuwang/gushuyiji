#!/usr/bin/python

from datetime import date


split_date = date(2012, 07, 15)
begin_date = date(2012, 04, 15)
date_delta_std = (split_date - begin_date).days

fin = open("input/input.csv")
train = open("output/train.csv", "w")
test = open("output/test.csv", "w")

fin.readline()
for line in fin.readlines():
    line = line.strip()
    entrys = line.split(",")
    entrys_date = date(int(entrys[3][0:4]), int(entrys[3][4:6]), int(entrys[3][6:8]))
    date_delta = (entrys_date - begin_date).days
    if date_delta < date_delta_std:
        train.write(",".join(entrys[:3]) + "," + str(date_delta) + "\n")
    elif 1 == int(entrys[2]):
        test.write(",".join(entrys[:2]) + "\n")

test.write("99999999999,9" + "\n")

test.close()
train.close()
fin.close()
