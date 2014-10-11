#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import json
import datetime
import commands

def isAleadyFinished(year,month,week):
    print year,month,week
    if not os.path.exists(year):
        return False
    if not os.path.exists(year+'/'+month):
        return False
    if not os.path.exists(year+'/'+month+'/'+week):
        return False
    return True

currentTime = str(datetime.datetime.now())
ymd = currentTime.split(' ')[0].split('-')
'''
year = int(ymd[0])
month = int(ymd[1])
day = int(ymd[2])
this_year, tot_week, week = datetime.date(year,month,day).isocalendar()
print week
'''
years = [ i for i in xrange(2010,2015) ]
months = [ i for i in xrange(1,13) ]
weeks = [ i for i in xrange(1,6) ]

for year in years:
    for month in months:
        for week in weeks:
            s_year = str(year)
            s_month = str(month)
            s_week = str(week)


            if isAleadyFinished(s_year,s_month,s_week):
                continue
#                exit(-1)

            if not os.path.exists(s_year):
                command = "mkdir %d" % year
                ret = commands.getoutput(command)
                print ret
            if not os.path.exists(s_year+'/'+s_month):
                command = "mkdir %d/%d" % (year,month)
                ret = commands.getoutput(command)
                print ret
            if not os.path.exists(s_year+'/'+s_month+'/'+s_week):
                command = "mkdir %d/%d/%d" % (year,month,week)
                ret = commands.getoutput(command)
                print ret

            for t_page in xrange(6):
                page = t_page + 1
                wget_command = "wget \"http://book.naver.com/bestsell/bestseller_list.nhn?cp=yes24&cate=001001027&bestWeek=%d-%d-%d&indexCount=7&type=list&page=%d\"" % (year,month,week,page)

                mv_command = "mv \"bestseller_list.nhn?cp=yes24&cate=001001027&bestWeek=%d-%d-%d&indexCount=7&type=list&page=%d\" \"%d.html\" " % (year,month,week,page,page)

                ret = commands.getoutput(wget_command)
                print ret
                ret = commands.getoutput(mv_command)
                print ret

                mv_command = "mv \"%d.html\" %d/%d/%d/" % (page,year,month,week)
                ret = commands.getoutput(mv_command)
                print ret
