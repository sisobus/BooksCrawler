#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import os
import sys

import datetime
import commands

def isAleadyFinished(year,month,week):
    print year,month,week
    if not os.path.exists('data/'+year):
        return False
    if not os.path.exists('data/'+year+'/'+month):
        return False
    if not os.path.exists('data/'+year+'/'+month+'/'+week):
        return False
    return True

currentTime = str(datetime.datetime.now())
ymd = currentTime.split(' ')[0].split('-')
year = int(ymd[0])
month = int(ymd[1])
day = int(ymd[2])
this_year, tot_week, week = datetime.date(year,month,day).isocalendar()

week = (day - 1) // 7 + 1

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

if not os.path.exists('json/%d/%d/%d/books.json' % (year,month,week)):
    print "it is not exists"

with open('json/%d/%d/%d/books.json' % (year,month,week) ) as fp:
    allBooks = json.loads(fp.read())

if not isAleadyFinished(s_year,s_month,s_week):
    if not os.path.exists('data/'+s_year):
        command = "mkdir data/%d" % year
        ret = commands.getoutput(command)
    #    print ret
    if not os.path.exists('data/'+s_year+'/'+s_month):
        command = "mkdir data/%d/%d" % (year,month)
        ret = commands.getoutput(command)
     #   print ret
    if not os.path.exists('data/'+s_year+'/'+s_month+'/'+s_week):
        command = "mkdir data/%d/%d/%d" % (year,month,week)
        ret = commands.getoutput(command)
      #  print ret 

f = open('data/%d/%d/%d/data.out' % (year,month,week),'w')

for book in allBooks:
    s = 'rank: '+str(book['rank'])
    #print s
    f.write(s+'\n')
    s = 'book_title: '+book['book_title']
    #print s
    f.write(s+'\n')
    s = 'img_url: '+book['img_url']
    #print s
    f.write(s+'\n')
    s = 'book_url: '+book['book_url']
    #print s
    f.write(s+'\n')
    s = 'body: '+book['body']
    #print s
    f.write(s+'\n')
    s = 'date: '+book['date']
    #print s
    f.write(s+'\n')
    s = 'star: '+str(book['star'])
    #print s
    f.write(s+'\n')
    authors = book['authors']
    for author in authors:
        if author['author_name'] <> None:
            s = 'author_name: '+author['author_name']
     #       print s
            f.write(s+'\n')
        s = 'author_url: '+str(author['author_url'])
      #  print s
        f.write(s+'\n')
    s = 'publisher: '+book['publisher']
    #print s
    f.write(s+'\n')
f.close()
