#!/usr/bin/python
#coding:utf-8
# Filename: read_csv.py

import csv

def read_csv(input_file):
    data = csv.reader(file(input_file,'rb'))
    output_file = open("outpu.txt","w")
    datalist = list()
    for row in data:
        if data.line_num == 1:
            continue
        datalist.append(row)
    iterator = 0
    while iterator < len(datalist):
        item_count = 0
        item = datalist[iterator + item_count]
        output_file.writelines(item[0] + ' ' + item[1])
        while iterator + item_count < len(datalist):
            item_temp = datalist[iterator + item_count]
            if item_temp[0] == item[0]:
                if item_temp[2] == '3':
                    output_file.writelines(',' + item_temp[1])
                item_count = item_count + 1
            else:
                break
        iterator += item_count
        output_file.writelines('\n')
       # output_file.writelines(item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + '\n')

if __name__ == '__main__':
    read_csv('t_alibaba_data.csv')


