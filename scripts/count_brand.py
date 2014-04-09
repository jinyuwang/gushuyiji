#!/usr/bin/python
#coding:utf-8
# Filename: read_csv.py

import csv

def read_csv(input_file):
    data = csv.reader(file(input_file,'rb'))
    output_file = open("outpu.txt","w")
    datalist = list()
    brand = list()
    for row in data:
        if data.line_num == 1:
            continue
        datalist.append(row)
    iterator = 0
    num = 0
    while iterator < len(datalist):
        item = datalist[iterator]
        if brand.count(item[1]) == 0:
                brand.append(item[1])
                num += 1
        iterator += 1
    print num
    print len(brand)

if __name__ == '__main__':
    read_csv('t_alibaba_data.csv')


