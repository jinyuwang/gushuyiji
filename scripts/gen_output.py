#!/usr/bin/python

test = open("output/test.csv")
result = open("output/pre.txt", "w")

entrys = test.readlines()
entrys.sort(key=lambda x: x.split(",")[0])
for index, entry in enumerate(entrys):
    uid, tid = entry.strip().split(",")
    if 0 == index:
        cur_id = uid
        cur_result = [tid]
    elif uid == cur_id:
        cur_result.append(tid)
    else:
        result.write(cur_id + "\t" + ",".join(set(cur_result)) + "\n")
        cur_id = uid
        cur_result = [tid]


result.close()
test.close()

