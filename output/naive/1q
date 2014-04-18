#/usr/bin/python

fin = open("result_new_id_3000_sorted.csv")
fout = open("result_new_id_3000_sorted_merged.csv", "w")

lines = fin.readlines()
for index, line in enumerate(lines):
    user_id = line.split("\t")[0]
    brand_id = line.strip().split("\t")[1]
    if index == 0:
        cur_uid = user_id
        cur_bids = [brand_id]
    elif user_id == cur_uid:
        cur_bids.append(brand_id)
    else:
        fout.write(cur_uid + "\t" + ",".join(cur_bids) + "\n")
        cur_uid = user_id
        cur_bids = [brand_id]
fin.close()
fout.close()
