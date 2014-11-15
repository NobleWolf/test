#!/usr/bin/python

f = open('programlist.txt', 'r')
pie = []

for pig in f:
    pie.append(int((pig.split())[1]))
    
print(pie)