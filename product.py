#a!/usr/bin/env python

def product(*lists):
    result = [[]]
    for next_list in lists:
        result = [e + [next_elem] for next_elem in next_list for e in result]
    for elem in result:
        yield tuple(elem)


if __name__ == '__main__':
    var1 = [1, 2, 3]
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

