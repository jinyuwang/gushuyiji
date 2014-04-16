#/usr/bin/python

#pick out from the prediction mark file

import sys

N_limit = int(sys.argv[1])
file_in = sys.argv[2]
file_out = sys.argv[3]

fin = open(file_in)
ftemp = open("temp___", "w")
fout = open(file_out, "w")

cnt = 0
fin.readline()
while (True):
    line = fin.readline()
    if 0 == len(line):
        break
    if cnt >= N_limit:
        break    

    line = line.strip().split(" ")
    ftemp.write(line[1] + "," + line[2] + "\n")
    
    cnt += 1

ftemp.write("999999999,-1\n")
ftemp.close()

ftemp = open("temp___")
entrys = ftemp.readlines()
entrys.sort(key=lambda x: x.split(",")[0])
for index, entry in enumerate(entrys):
    uid ,tid = entry.strip().split(",")
    if 0 == index:
        cur_id = uid
        cur_result = [tid]
    elif uid == cur_id:
        cur_result.append(tid)
    else:
        fout.write(cur_id + "\t" + ",".join(set(cur_result)) + "\n")
        cur_id = uid
        cur_result = [tid]

ftemp.close()
fout.close()
fin.close()


