#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import os
from bs4 import BeautifulSoup

import datetime
import commands

def isAleadyFinished(year,month,week):
    #print year,month,week
    if not os.path.exists('json/'+year):
        return False
    if not os.path.exists('json/'+year+'/'+month):
        return False
    if not os.path.exists('json/'+year+'/'+month+'/'+week):
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

if not os.path.exists('json/'+s_year):
    command = "mkdir json/%d" % year
    ret = commands.getoutput(command)
if not os.path.exists('json/'+s_year+'/'+s_month):
    command = "mkdir json/%d/%d" % (year,month)
    ret = commands.getoutput(command)
if not os.path.exists('json/'+s_year+'/'+s_month+'/'+s_week):
    command = "mkdir json/%d/%d/%d" % (year,month,week)
    ret = commands.getoutput(command)

allBook = []
allHtmlSize = 6
rank = 1
for i in xrange(allHtmlSize+1):
    if i == 0:
        continue
    if not os.path.exists('html/%d/%d/%d/%d.html'% (year,month,week,i)):
        print "It is not exists"
        continue
    if os.path.exists('json/%d.json'%i):
        print "json is already exists"
        continue

    with open('html/%d/%d/%d/%d.html'% (year,month,week,i)) as fp:
        s = fp.read()
    soup = BeautifulSoup(s)
    ol = soup.find('ol')
    if ol == None:
        print "error : ol is none!"
        continue
    lis = ol.find_all('li')

    for li in lis:
        img_src = (li.find_all('a'))[0].find('img')['src']
        dt = li.find('dt')
        book_url = dt.find('a')['href']
        book_title = dt.find('a').string

        dds = li.find_all('dd')
        date = dds[0].contents[-1].lstrip().rstrip()

        star = dds[1].contents[2].lstrip().rstrip()

        authors = []
        aa = dds[0].find_all('a')
        publisher = ""
        if dds[0].contents[-3] <> None:
            publisher = dds[0].contents[-3].lstrip().rstrip()
        else:
            publisher = ""
        for a in aa:
            now = a['href']
            now = now.lstrip().rstrip()
            t = {
                    'author_name':a.string,
                    'author_url':now
                    }
            authors.append(t)
        body = dds[2].contents[2]
        t = {
                'img_url':img_src,
                'book_url':book_url,
                'book_title':book_title,
                'authors':authors,
                'body':body,
                'date':date,
                'rank':rank,
                'star':star,
                'publisher':publisher
                }
        allBook.append(t)
        rank = rank+1

#for b in allBook:
#    print b

with open('json/%d/%d/%d/books.json' % (year,month,week),'w') as fp:
    fp.write(json.dumps(allBook));
