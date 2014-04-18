#!/usr/bin/python

fin = open("input_sorted_index.csv")
fout = open("input_sorted_index_new.csv", "w")

lines = fin.readlines()
lines.sort(key=lambda x:(int(x.split(",")[0]), int(x.split(",")[1])))
