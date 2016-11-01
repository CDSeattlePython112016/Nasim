#Build an algorithm for Bubble Sort
import random

myList = []
for count in range (100):
    myList.append(int(random.random()*10000))
    print "unsorted: ", myList

for i in xrange(len(myList)-1,0,-1):
    for j in xrange(i):
        if myList[j] > myList[j + 1]:
            (myList[j], myList[j+1])=(myList[j+1], myList[j])
print "sorted:", myList
print myList == sorted(myList)
