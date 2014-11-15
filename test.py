#!/usr/bin/python

import sys
prgmlst = open('programlist.txt', 'r')

print 'Number os arguments: ', len(sys.argv)
print 'Argument List: ', str(sys.argv)
print prgmlst

memSize = 512

class programList:
    prgmOrderNum = []
    prgmNameNum = []

    def loadPrgmLst(self):
        f = open('programlist.txt', 'r')
        for list in f:
            temp = list.split()
            (temp[0])

