#!/usr/bin/python


users = 0
brands = 0

f = open("output/pre.txt")
for line in f.readlines():
    line = line.strip()
    uid, bid = line.split("\t")
    bids = bid.split(",")
    users += 1
    brands += len(bid)
    

f.close()

print "predict users: ", users
print "predict brands:", brands
