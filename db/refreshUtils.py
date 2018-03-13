#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : joker

import sys,os
sys.path.append('..')
import requests,re,sqlite3,time
import dataManager
from net import refreshNet
import keys



def insertDataList(listData,lang):
    conn = sqlite3.connect(getPath(lang))
    cursor = conn.cursor()
    for data in listData:
        try:
            cursor.execute('''insert into repos values("%s","%s",%d,%d,"%s","%s","%s")'''
            %(data['repo'],data['lang'],
            dataManager.parseInt(data['stars'].replace(',','')),
            dataManager.parseInt(data['forks'].replace(',','')),
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            data['repo_link'],data['desc']))
        except Exception as err:
            print err
    conn.commit()
    conn.close()

def selectDBSelf(repo,lang):
    one = None
    conn = sqlite3.connect(getPath(lang))
    cursor = conn.cursor()
    try:
        cursor.execute('''select * from repos where repo = "%s"''' %(repo))
        one = cursor.fetchone()
    except Exception as err:
        print err
    conn.commit()
    conn.close()
    return one

def createDB(lang):
    if not os.path.exists(getPath(lang)):
        conn = sqlite3.connect(getPath(lang))
        cursor = conn.cursor()
        cursor.execute('''create table repos (repo text primary key, lang text, stars int, forks int, update_time text, repo_link text, desc text)''')
        conn.commit()
        conn.close()

def getPath(lang):
    return '/Users/joker/workSpace/db/%sCache.db' %lang


def createRepo(row):
    repo = {}
    repo['repo'] = row[0]
    repo['lang'] = row[1]
    repo['stars'] = str(row[2])
    repo['forks'] = str(row[3])

    repo['repo_link'] = row[5]
    repo['desc'] = row[6]
    return repo
