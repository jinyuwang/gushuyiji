#!/usr/bin/python
from datetime import date
splitdate = date(2013,8,1)

users = []
brands = []
num_of_users = 0
num_of_brands = 0
user_brand_table = {}

def count():
    global users
    global brands
    global num_of_users
    global num_of_brands
    fin = open("../../output/naive/input_sorted.csv")
    items = fin.readlines()
    for item in items:
        user_index = item.split(",")[0]
        brand_index = item.split(",")[1]
        users.append(user_index)
        brands.append(brand_index)
    users = list(set(users))
    brands = list(set(brands))
    users.sort(key=int)
    brands.sort(key=int)
    num_of_users = len(users)
    num_of_brands = len(brands)
    print num_of_users
    print num_of_brands
    fin.close()


def calculate():
    global num_of_brands
    global user_brand_table
    fin = open("../../output/naive/input_sorted_index.csv")
    fout = open("../../output/naive/result_new.csv", "w")

    items = fin.readlines()
    for item in items:
        user_index = int(item.split(",")[0])
        brand_index = int(item.split(",")[1])
        type_id = item.split(",")[2]
        user_brand_table[user_index * num_of_brands + brand_index] = 0

    for item in items:
        user_index = int(item.split(",")[0])
        brand_index = int(item.split(",")[1])
        print user_index, brand_index
        type_id = int(item.split(",")[2])
        item_date = date(2013, int(item.split(",")[3]), int(item.split(",")[4]))
        if type_id == 1 and item_date < splitdate:
            user_brand_table[user_index * num_of_brands + brand_index] += 3
        elif type_id == 1 and item_date >= splitdate:
            user_brand_table[user_index * num_of_brands + brand_index] += -1
        elif type_id == 2:
            user_brand_table[user_index * num_of_brands + brand_index] += 2
        elif type_id == 3:
            user_brand_table[user_index * num_of_brands + brand_index] += 1
        else:
            user_brand_table[user_index * num_of_brands + brand_index] += 2.0/(date(2013,8,16)-item_date).days

    for item in user_brand_table:
        print item
        fout.write(str(int(item)/num_of_brands) + " " + str(int(item)%num_of_brands) + " " + str(user_brand_table[item]) + "\n")

    fin.close()
    fout.close()

def top_N(num):
    global users
    global brands
    global num_of_brands
    global user_brand_table
    fout = open("../../output/naive/result_new_" + str(num) + ".csv", "w")
    fout2 = open("../../output/naive/result_new_id_" + str(num) + ".csv", "w")
    result = sorted(user_brand_table.items(), key=lambda d:int(d[1]), reverse=True)
 #   print result
    i = 0
    for item,nu in result:
        print item
        if i < num:
            fout.write(str(int(item)/num_of_brands) + " " + str(int(item)%num_of_brands) + " " + str(nu) + "\n")
            fout2.write(str(users[(int(item)/num_of_brands)]) + "\t" + str(brands[(int(item)%num_of_brands)]) + "\n")
            i += 1
    fout2.write("99999999999999999999999999999999\t9999999999999999999999999999999999999\n")
    fout.close()
    fout2.close()

count()
calculate()
top_N(3000)
