#!/usr/bin/python

from datetime import date

year = 2013
split_date1 = date(year, 05, 15)
split_date2 = date(year, 06, 15)
split_date3 = date(year, 07, 15)
begin_data = date(year, 04, 15)
date_delta1 = (split_data1 - begin_data).days
date_delta2 = (split_data2 - begin_data).days
date_delta3 = (split_data3 - begin_data).days


fin = open("input/input.csv")
mid_output_strategy_circle = open("output/output_strategy_circle/mid_output_strategy_circle.csv","w")
fout = open("out/output_strategy_circle.csv", "w")

def judge_date(delt):
    if delt <= date_delta1:
        return 1
    elif delt >= date_delta1  && delt <= date_delta2:
        return 2
    elif delt >= date_delta2  && delt <= date_delta3:
        return 3
    else
        return 4

def strategy_circle_stage1():
    fin.readline()
    entrys = fin.readlines()
    entrys.sort(key=lambda x: x.split(",")[0])
    for index, entry in enumerate(entrys):
        entry  = entry.strip().split(",")
        uid = entry[0]
        tid = entry[1]
        entry_date = date(year, int(entry[3]), int(entry[4]))
        date_delta = (entry_date - begin_data).days
        if 0 == index:
            cur_id = uid
            cur_tid = tid
            cur_date = [judge_date(date_delta)]
        elif uid == cur_id && tid == cur_tid:
            cur_date.append(judge_date(date_delta))
        else:
            num =  len(set(cur_date))
            if num == 4:
                mid_output_strategy_circle.write(cur_id + "," + cur_tid + "," + "4" + "\n")
                cur_id = uid
                cur_tid = tid
                cur_date = [judge_date(date_delta)]
            elif num == 3:
                mid_output_strategy_circle.write(cur_id + "," + cur_tid + "," + "3" + "\n")
                cur_id = uid
                cur_tid = tid
                cur_date = [judge_date(date_delta)]
            elif num == 2:
                mid_output_strategy_circle.write(cur_id + "," + cur_tid + "," + "2" + "\n")
                cur_id = uid
                cur_tid = tid
                cur_date = [judge_date(date_delta)]
            elif num == 1 && 4 in cur_date:
                mid_output_strategy_circle.write(cur_id + "," + cur_tid + "," + "0" + "\n")
                cur_id = uid
                cur_tid = tid
                cur_date = [judge_date(date_delta)]
            else:
                mid_output_strategy_circle.write(cur_id + "," + cur_tid + "," + "1" + "\n")
                cur_id = uid
                cur_tid = tid
                cur_date = [judge_date(date_delta)]
    mid_output_strategy_circle.close()
    fin.close()

def strategy_circle_stage2():
    mid_input = open("mid_output_strategy_circle.csv")
    for index, entry in enumerate(mid_input.readlines()):
        uid, tid, weight = entry.strip().split(",")
        if 0 == index:
            cur_id = uid
            cur_result = [t]






