#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# 
########################################################################
 
"""
File: G.py
Author: AngelClover(AngelClover@aliyun.com)
Date: 2014/11/20 02:33:45
"""
#!/usr/bin/python
#coding=utf-8
import logging
from logging import debug
import string

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    debug ((__file__, "is running"))
    while 1:
        try:
            line = raw_input()
            li = line.split()
            ab = string.atoi(li[0])
            ac = string.atoi(li[1])
            bd = string.atoi(li[2])
            tt = bd - ac
            #at = ab * ac / tt
            up = ab * ac
            d = gcd(up, tt)
            print "%d/%d" % (up/d, tt/d)
        except Exception,e:
            break

