#!/usr/bin/python
import os, sys, datetime

def merge_file(fdir, fileoutput):
    file_list = os.listdir(fdir)
    file_to_write = open(fileoutput, "w")
    for fp in file_list:
        file_to_read = open(fdir + str(fp))
        for line in file_to_read.readlines():
            file_to_write.write(line)
    file_to_write.close()

def merge_data(fileinput, finaloutput):
    fin = open(fileinput)
    fout = open(finaloutput,"w")
    lines = fin.readlines()
    lines.sort(key=lambda x: int(x.split("\t")[0]))
    for index, line in enumerate(lines):
        uid = line.strip().split("\t")[0]
        items = (line.strip().split("\t")[1]).split(",")
        if index == 0:
            cur_id = uid
            cur_items = items
        elif uid == cur_id:
            cur_items = cur_items + items
        else:
            cur_items = list(set(cur_items))
            cur_items.sort(key=int)
            fout.write(cur_id + "\t" + ",".join(cur_items) + "\n")
            cur_id = uid
            cur_items = items
    fin.close()
    fout.close()

def merge(fdir, file_output):
    merge_file(fdir, "mid_output.csv")
    merge_data("mid_output.csv", file_output)


fdir = raw_input('>>>Input the directory name you want to merge:\n>>>')
cur = datetime.datetime.now()
file_output = "pre" + "_" + str(cur.year) + "_" + str(cur.month) + "_" + str(cur.day) + "_" + str(cur.hour) + "_" + str(cur.minute) + ".txt"
merge(fdir,file_output)
print ">>>Done"
print ">>>A new file is created " + file_output
