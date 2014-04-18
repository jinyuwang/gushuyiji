#/usr/bin/python

import sys
import math

ftrain = sys.argv[1]
recommend_users = int(sys.argv[2])
max_nums_per_user = int(sys.argv[3])

train = {}

def ItemSimilarity(train):
    C = dict()
    N = dict()
    W = dict()
    for u, items in train.items():
        for i in items:
            if i not in N:
                N[i] = 0
            N[i] += 1
            for j in items:
                if i == j:
                    continue
                if i not in C:
                    C[i] = {}
                if j not in C[i]:
                    C[i][j] = 0
                C[i][j] += 1

    for i, related_items in C.items():
        for j, cij in related_items.items():
            if i not in W:
                W[i] = {} 
            if j not in W[i]:
                W[i][j] = 0
            W[i][j] = cij / math.sqrt(N[i] * N[j])

    return W


def Recommendation(train, user_id, W, K):
    rank = dict()
    ru = train[user_id]
    for i in ru:
        for j, wj in sorted(W[i].items(), key = lambda var:var[1], reverse = True)[0:K]:
            if j in ru:
                continue
            if j not in rank:
                rank[j] = 0
            rank[j] += wj

    return sorted(rank.items(), key = lambda var:var[1], reverse =True)


#train = {
#            1 : ['a', 'b', 'd'],
#            2 : ['b', 'c', 'e'],
#            3 : ['c', 'd'],
#            4 : ['b', 'c', 'd'],
#            5 : ['a', 'd'] 
#        }

fin = open(ftrain)
cnt = 0
while True:
    line = fin.readline()
    if 0 == len(line):
        break
    if cnt >= recommend_users:
        break
    cnt += 1
    uindex, brand = line.strip().split(" ")
    brands = brand.split(",")
    train[uindex] = brands

#print "train:"
#print train


W = ItemSimilarity(train)
#print "\nW:"
#print W
#print "\nrank:"
for uindex, items in train.items():
    rank = Recommendation(train, uindex, W, 5)
    #print rank
    res = ""
    index_list = []
    for index, ra in rank:
        if max_nums_per_user == len(index_list):
            break
        index_list.append(index)

    print str(uindex) + "\t" + ",".join(index_list)
