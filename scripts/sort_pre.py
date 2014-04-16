#/usr/bin/python

#pick out from the prediction mark file

import sys

user_num = 4

user_id_list = []
brand_id_list = []
user_index_list = []
brand_index_list = []
mark_index = {}
index = 0

file_in = sys.argv[1]
file_test = sys.argv[2]
file_out_index = sys.argv[3]
file_out_id = sys.argv[4]
fin = open(file_in)
ftest = open(file_test)
fout_index = open(file_out_index, "w")
fout_id = open(file_out_id, "w")
fu = open("user_id.csv")
fb = open("brand_id.csv")


fu.readline()
for line in fu.readlines():
    user_id_list.append(line.strip())
fu.close()

fb.readline()
for line in fb.readlines():
    brand_id_list.append(line.strip())
fb.close()

for line in ftest.readlines():
    line = line.split(" ")
    user = line[1].split(":")
    brand = line[2].split(":")
    user_index_list.append(int(user[0]))
    brand_index_list.append(int(brand[0]) - user_num)
ftest.close()

for line in fin.readlines():
    mark_index[float(line)] = index
    index += 1
fin.close()

mark_list = sorted(mark_index.iteritems(), key = lambda var:var[0], reverse = True)

###debug
fd_mark = open("mark_list.csv", "w")
fd_user_index = open("user_index.csv", "w")
fd_brand_index = open("brand_index.csv", "w")
fd_user_id = open("user_id_list.csv", "w")
fd_brand_id = open("brand_id_list.csv", "w")

fd_mark.write("p line_num\n")
for li in mark_list:
    fd_mark.write(str(li[0]) + " " + str(li[1]) + "\n")

fd_user_id.write("user_id\n")
for li in user_id_list:
    fd_user_id.write(li + "\n")

fd_brand_id.write("brand_id\n")
for li in brand_id_list:
    fd_brand_id.write(li + "\n")

fd_user_index.write("user_index\n")
for li in user_index_list:
    fd_user_index.write(str(li) + "\n")

fd_brand_index.write("brand_index\n")
for li in brand_index_list:
    fd_brand_index.write(str(li) + "\n")

fd_mark.close()
fd_brand_id.close()
fd_user_id.close()
fd_brand_index.close()
fd_user_index.close()
###debug

fout_index.write("p line_num u_index b_index\n")
for li in mark_list:
    fout_index.write(str(li[0]) + " " + str(li[1]) + " " + str(user_index_list[li[1]]) + " " + str(brand_index_list[li[1]]) + "\n")

fout_id.write("p uid bid\n")
for li in mark_list:
    fout_id.write(str(li[0]) + " " + str(user_id_list[user_index_list[li[1]]]) + " " + str(brand_id_list[brand_index_list[li[1]]]) + "\n")

fout_index.close()
fout_id.close()

