#!/usr/bin/python3

print("fibonacci number?")

num = int(input())

def fibonacci(n):
    if n<3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    print(fibonacci(n))

for i in range(1,num+1):
    print(fibonacci(i), end=' ')

print("\nF",num,"= ",fibonacci(num))
