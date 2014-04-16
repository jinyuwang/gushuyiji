#/usr/bin/python

#pick out from the prediction mark file

import sys

user_id_list = []
brand_id_list = []
user_index_list = []
brand_index_list = []
mark_index = {}
index = 0


file_in = sys.argv[1]
file_test = sys.argv[2]
file_out = sys.argv[3]
fin = open(file_in)
ftest = open(file_test)
fout = open(file_out, "w")
fu = open("../input/user_id.csv")
fb = open("../input/brand_id.csv")

fu.readline()
for line in fu.readlines():
    user_id_list.append(line.strip())

fb.readline()
for line in fb.readlines():
    brand_id_list.append(line.strip())

for line in ftest.readlines():
    line = line.split(" ")
    user = line[0].split(":")
    brand = line[1].split(":")
    user_index_list.append(int(user[0]))
    brand_index_list.append(int(brand[0]))

for line in fin.readlines():
    mark_index[float(line)] = index
    index += 1

mark_list = sorted(mark_index.iteritems(), key = lambda var:var[0], reverse = True)

#print user_id_list
#print brand_id_list
#print user_index_list
#print brand_index_list
#print mark_list

fout.write("p uid bid\n")
for li in mark_list:
    fout.write(str(li[0]) + " " + str(user_id_list[user_index_list[li[1]]]) + " " + str(brand_id_list[brand_index_list[li[1]]]) + "\n")

fout.close()
fin.close()

