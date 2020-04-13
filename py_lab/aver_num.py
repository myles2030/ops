#!/usr/bin/python3

print("How many numbers will you type??")

num = int(input())

a = []

a = input().split()

for i in range(num):
    a[i] = int(a[i])

AVG = sum(a)/num

print(AVG)
