#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import os
import sys

import datetime
import commands
import sqlite3



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
#print ymd
#print datetime.date(year,month,day).isocalendar()
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


if not os.path.exists('db/'+s_year):
    command = "mkdir db/%d" % year
    ret = commands.getoutput(command)
 #   print ret
if not os.path.exists('db/'+s_year+'/'+s_month):
    command = "mkdir db/%d/%d" % (year,month)
    ret = commands.getoutput(command)
  #  print ret
if not os.path.exists('db/'+s_year+'/'+s_month+'/'+s_week):
    command = "mkdir db/%d/%d/%d" % (year,month,week)
    ret = commands.getoutput(command)
  #  print ret
if os.path.exists('db/'+s_year+'/'+s_month+'/'+s_week+'/'+'ok'):
    exit(-1)

if not os.path.exists('db/'+s_year+'/'+s_month+'/'+s_week+'/'+'ok'):
    command = "touch db/%d/%d/%d/ok" % (year,month,week)
    ret = commands.getoutput(command)
   # print ret

db = sqlite3.connect('info.sqlite')
cur = db.cursor()    
#cur.execute('SELECT SQLITE_VERSION()')

query = 'CREATE TABLE "book_kid_%d_%d"("RANKING" INTEGER PRIMARY KEY NOT NULL, "BOOK_NAME" TEXT, "AUTHOR" TEXT, "STAR" FLOAT, "IMAGE_URL" TEXT, "ISBN" INTEGER, "PUBLISHER" TEXT, "PUB_DATE" TEXT)' % (month,week)
cur.execute(query)

if not os.path.exists('json/%d/%d/%d/books.json' % (year,month,week)):
    print "it is not exists"

with open('json/%d/%d/%d/books.json' % (year,month,week) ) as fp:
    books = json.loads(fp.read())

#ret = ""
for book in books:
    rank = book['rank']
    book_name = book['book_title']
    author = book['authors'][0]['author_name']
    star = book['star']
    image_url = book['img_url']
    publisher = book['publisher']
    pub_date = book['date']
    query = 'INSERT INTO book_kid_%d_%d("RANKING","BOOK_NAME","AUTHOR","STAR","IMAGE_URL","PUBLISHER","PUB_DATE") VALUES (%d,"%s","%s","%s","%s","%s","%s"); ' % (month,week,rank,book_name,author,star,image_url,publisher,pub_date)
#    print query
    #ret = ret + query
    #cur = db.cursor()    
    cur.execute(query)
    db.commit()

#print ret
