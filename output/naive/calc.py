#/usr/bin/python

#calculate pre users and brands

import sys

file_in = sys.argv[1]

users = 0
brands = []
brands_sum = 0

f = open(file_in)

for line in f.readlines():
    line = line.strip()
    uid, bid = line.split("\t")
    bids = bid.split(",")
    users += 1
    brands_sum += len(bids)
    for bid_iter in bids:
        if bid_iter not in brands:
            brands.append(bid_iter)

f.close()

print "predict users:     ", users
print "predict brands:    ", len(brands)
print "predict brands_sum:", brands_sum
