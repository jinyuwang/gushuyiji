#!/usr/bin/python
#coding:utf-8

def read_data(input_data,output):
    file_in = open(input_data,'r')
    file_out = open(output,"w")
    lines = file_in.readlines()
    result = list()
    for line in lines:
        line = line.decode('GBK')
        line = line.encode('UTF-8')
        print line
        file_out.write(line)
        result.append(line)
    print result
    file_in.close()
    file_out.close()

read_data('t_alibaba_data.csv','output.txt')

