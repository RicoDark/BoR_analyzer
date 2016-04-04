#!/usr/bin/python
# coding: utf8

from datetime import datetime

def BoR_Time (brt):
    return datetime(int(brt[0:4]), int(brt[5:7]), int(brt[8:10]),
                    int(brt[11:13]), int(brt[14:16]), int (brt[17:19]))
