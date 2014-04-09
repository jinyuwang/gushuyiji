#!/usr/bin/python


fin = open("input/t_alibaba_data.csv")
fout = open("input/input.csv", "w")

fout.write("user_id,brand_id,type,visit_datetime\n")

fin.readline()
for line in fin.readlines():
    line = line.strip()
    entrys = line.split(",")
    date = entrys[3]
    date = date.decode("gbk")
    month = date[0]
    
    if 5 == len(date):
        day = 10 * int(date[2]) + int(date[3])
        day = str(day)
    else:
        day = int(date[2])
        day = "0" + str(day)
    
    entrys[3] = "2012" + "0" + month + day
    fout.write(",".join(entrys) + "\n")

fin.close()
fout.close()
