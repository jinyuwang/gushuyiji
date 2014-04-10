#!/usr/bin/python


fin = open("input/t_alibaba_data.csv")
fout = open("input/input.csv", "w")

fout.write("user_id,brand_id,type,month,day\n")

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
    
    fout.write(entrys[0] + "," + entrys[1] + "," + entrys[2] + ",0" +  month + "," + day + "\n")

fout.close()
fin.close()
