#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: F.py
Author: changhaozhe(changhaozhe@baidu.com)
Date: 2014/11/16 15:35:01
"""
#!/usr/bin/python
#coding=utf-8
import logging
from logging import debug
           

class Julian:
    #mm = [31,28,31,30,31,30,31,31,30,31,30,31]
    def __init__(self, year, month, day):
        t = year * 365 + (year+3) / 4
        if year%4 == 0:
            is_leap = 1
        else:
            is_leap = 0
        #print t
        mm = self.get_mm( is_leap )
        #print month,day,is_leap,mm
        for i in range(1,month):
            #print t,t,mm[i-1]
            t += mm[i - 1]
        t += day
        self.days = t

    def run(self):
        #print "total day:%d" % self.days
        return self.days

    def get_mm(self, is_leap):
        return [31,28+is_leap,31,30,31,30,31,31,30,31,30,31]
        

class Gregorian:
    #mm = [31,28,31,30,31,30,31,31,30,31,30,31]
    def calc(self):
        t = self._days

        d = t / (365*400 + 100 - 4 + 1)
        year = d * 400
        t -= d * (365*400 + 100 - 4 + 1)

        for i in range(0,400):
            if i == 0:
                leap = 1
            elif i%100 == 0:
                leap = 0
            elif i%4 == 0:
                leap = 1
            else:
                leap = 0
            td = 365 + leap
            if t <= td :
                is_leap = leap
                break
            else:
                t-=td
                year += 1

        mm = self.get_mm( is_leap )

        #print year,t,mm,is_leap
        for i in range (0,12):
            if t <= mm[i]:
                month = i+1
                break
            t -= mm[i]
        day = t
        print "%d-%02d-%02d" % (year,month,day)
    def __init__(self, _days):
        self.days = _days
        #self.calc()
        self.calc1()
        #self.calc2()
    def is_leap(self,year):
        if year%400 == 0:
            leap = 1
        elif year%100 == 0:
            leap = 0
        elif year%4 == 0:
            leap = 1
        else:
            leap = 0
        return leap

    def getday(self, year):
        return 365 + self.is_leap(year)
    
    def getmm(self,year):
        return [31,28+self.is_leap(year),31,30,31,30,31,31,30,31,30,31]

    def this100year(self, year):
        return 365*100 + 24 + self.is_leap(year)

    def calc1(self):
        t = self.days
        d = (t-1) / (365*400 + 100 - 4 + 1)
        year = d * 400
        t -= d * (365*400 + 100 - 4 + 1)

        while t > self.this100year(year):
            t -= self.this100year(year)
            year += 100

        tmp = 0
        while t > self.getday(year):
            #print "year:%d day:%d" % (year,self.getday(year+1))
            if tmp == 1:
                d = (t-1) / (365*4 + 1)
                t -= d * (365*4 + 1)
                year += d * 4
            else:
                t -= self.getday(year)
                year += 1
            tmp += 1

        mm = self.getmm(year)
        month = 1
        while t > mm[month-1]:
            t -= mm[month-1]
            month += 1
        day = t
        print "%d-%02d-%02d" % (year,month,day)

    def calc2(self):
        t = self.days
        year = 0
        while t > self.getday(year):
            #print "year:%d day:%d" % (year,self.getday(year+1))
            t -= self.getday(year)
            year += 1

        mm = self.getmm(year)
        month = 1
        while t > mm[month-1]:
            t -= mm[month-1]
            month += 1
        day = t
        print "%d-%02d-%02d" % (year,month,day)
        
    def get_mm(self,is_leap):
        if is_leap > 1:
            is_leap = 1
        return [31,28+is_leap,31,30,31,30,31,31,30,31,30,31]

        




if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)
    #debug ((__file__, "is running"))


    import string
    #try:
    while 1:
        try:
            ss = raw_input("")
        except Exception,e:
            break
        if ss == "":
            break
        l = ss.split('-')
        ju = Julian(string.atoi(l[0]), string.atoi(l[1]), string.atoi(l[2]))
        Gregorian(ju.run()-1)
    #except:
        
        
