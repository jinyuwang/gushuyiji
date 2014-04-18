#!/usr/bin/python

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
    fout = open("../../output/naive/result.csv", "w")

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
        if type_id == 1:
            user_brand_table[user_index * num_of_brands + brand_index] += 5
        elif type_id == 2:
            user_brand_table[user_index * num_of_brands + brand_index] += 2
        elif type_id == 3:
            user_brand_table[user_index * num_of_brands + brand_index] += 3
        else:
            user_brand_table[user_index * num_of_brands + brand_index] += 1

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
    fout = open("../../output/naive/result_" + str(num) + ".csv", "w")
    fout2 = open("../../output/naive/result_id_" + str(num) + ".csv", "w")
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
