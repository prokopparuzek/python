#!/usr/bin/python3
for i in range(1,int(2**64)):
    c = 0
    test = False
    for j in range(10,100):
        if i % j == 0 and int(j/100) == 0:
            c += 1
            if j == 60:
                test = True
    if c >= 73:
        print("{} dělitelů {}".format(c, j))
    if test and c >= 73:
        print("i 60")
