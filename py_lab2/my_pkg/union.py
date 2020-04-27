#!/usr/bin/python3

def listfunc():
    print("1st list: ")
    firstlist1 = str(input())
    firstlist2 = firstlist1.replace("["," ").replace("]"," ").replace(","," ").split()
    firstlist3 = list(firstlist2)
    firstlist4 = set(list(map(int,firstlist3)))
    
    print("2st list: ")
    secondlist1 = str(input())
    secondlist2 = secondlist1.replace("["," ").replace("]"," ").replace(","," ").split()
    secondlist3 = list(secondlist2)
    secondlist4 = set(list(map(int,secondlist3)))

    print("=> union", list(firstlist4.union(secondlist4)))

    print("=> intersection: ", list(firstlist4.intersection(secondlist4)))



