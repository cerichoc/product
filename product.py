#a!/usr/bin/env python

def product(*allvar):
    nList = len(allvar)

    i = 0
    for elem1 in allvar[i]:
        mylist =[]
        mylist.append(elem1)
        for j in xrange(i+1,nList):
            myNewList = []
            for nb in xrange(len(mylist)):
                for x in xrange(len(allvar[j])):
                    if j==i+1:
                        myNewList.append([mylist[nb]])  
                    else:
                        myNewList.append(mylist[nb][:])  
            mylist = myNewList[:]

            for nbelem2, elem2 in enumerate(allvar[j]):
                for val in xrange(nbelem2, len(mylist), len(allvar[j])):
                    mylist[val].append(elem2)
        for elem in mylist:
            yield tuple(elem)


if __name__ == '__main__':
    var1 = [1,2,3]
    var2 = ["a", "b"]
    var3 = ["x", "y", "z"]
    var4 = [9,8,7,6,5]

    globalList = product(var1, var2, var3, var4)

    from itertools import product
    test = product(var1, var2, var3, var4)

    assert sorted(test) == sorted(globalList)

    print(" \n")

    #print len(globalList)

    for elem in globalList:
        print elem

    for elem in test:
        print elem

