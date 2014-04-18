#!/usr/bin/python

fin = open("result_new_id_3000.csv")
fout = open("result_new_id_3000_sorted.csv", "w")

lines = fin.readlines()
lines.sort(key=lambda x: (int(x.split("\t")[0]), int(x.split("\t")[1])))
fout.writelines(lines)

fin.close()
fout.close()
