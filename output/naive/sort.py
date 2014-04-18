#!/usr/bin/python

fin = open("result_3000.csv")
fout = open("result_3000_sorted.csv", "w")

lines = fin.readlines()
lines.sort(key=lambda x: (int(x.split(" ")[0]), int(x.split(" ")[1])))
fout.writelines(lines)

fin.close()
fout.close()
