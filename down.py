#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import json
import datetime
import commands

def isAleadyFinished(year,month,week):
    print year,month,week
    if not os.path.exists('html/'+year):
        return False
    if not os.path.exists('html/'+year+'/'+month):
        return False
    if not os.path.exists('html/'+year+'/'+month+'/'+week):
        return False
    return True

currentTime = str(datetime.datetime.now())
ymd = currentTime.split(' ')[0].split('-')
year = int(ymd[0])
month = int(ymd[1])
day = int(ymd[2])
this_year, tot_week, week = datetime.date(year,month,day).isocalendar()

week = (day - 1) // 7 +1

if week == 1:
    if month == 1:
        year = year - 1
        month = 12
        week = 5
    else:
        month = month - 1
        week = 5
else:
    week = week - 1
#print week

s_year = str(year)
s_month = str(month)
s_day = str(day)
s_week = str(week)
if isAleadyFinished(s_year,s_month,s_week):
    exit(-1)

if not os.path.exists(s_year):
    command = "mkdir html/%d" % year
    ret = commands.getoutput(command)
    #print ret
if not os.path.exists(s_year+'/'+s_month):
    command = "mkdir html/%d/%d" % (year,month)
    ret = commands.getoutput(command)
    #print ret
if not os.path.exists(s_year+'/'+s_month+'/'+s_week):
    command = "mkdir html/%d/%d/%d" % (year,month,week)
    ret = commands.getoutput(command)
    #print ret

for t_page in xrange(6):
    page = t_page + 1
    wget_command = "wget \"http://book.naver.com/bestsell/bestseller_list.nhn?cp=yes24&cate=001001027&bestWeek=%d-%d-%d&indexCount=7&type=list&page=%d\"" % (year,month,week,page)
    
    mv_command = "mv \"bestseller_list.nhn?cp=yes24&cate=001001027&bestWeek=%d-%d-%d&indexCount=7&type=list&page=%d\" \"%d.html\" " % (year,month,week,page,page)

    ret = commands.getoutput(wget_command)
    #print ret
    ret = commands.getoutput(mv_command)
    #print ret

    mv_command = "mv \"%d.html\" html/%d/%d/%d/" % (page,year,month,week)
    ret = commands.getoutput(mv_command)
    #print ret
