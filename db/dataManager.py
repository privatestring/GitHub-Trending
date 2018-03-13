#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : joker

import sqlite3,sys,os,time
sys.path.append("..")
import keys

TAB_NAME = 'repos'

def manager(listData):
    createDB()
    if listData is not None:
        conn = sqlite3.connect(keys.DB_SAVE_PATH)
        cursor = conn.cursor()
        for data in listData:
            if data is not None:
                insertOrUpdate(conn,cursor,data)
        conn.close()

def createDB():
    if not os.path.exists(keys.DB_SAVE_PATH):
        conn = sqlite3.connect(keys.DB_SAVE_PATH)
        cursor = conn.cursor()
        cursor.execute('''create table "%s" (repo text primary key, lang text, stars int, forks int, update_time text, repo_link text, desc text)''' %TAB_NAME)
        conn.commit()
        conn.close()

def insertOrUpdate(conn,cursor,data):
    row = selectDB(conn,cursor,data['repo'])
    if checkDataChanged(conn,cursor,data,row) :
        deleteDB(conn,cursor,data['repo'])
        insertDB(conn,cursor,data)
        print "old delete insert new  "+ data['repo']
    elif row is None:
        insertDB(conn,cursor,data)
        print "first insert  "+ data['repo']
    else :
        print "no changed  "+ data['repo']

    # if len(selectDB(conn,cursor,data['repo'])) > 0:
    #     deleteDB(conn,cursor,data['repo'])
    # insertDB(conn,cursor,data)

def checkDataChanged(conn,cursor,data,row):
    stars = parseInt(data['stars'].replace(',',''))
    forks = parseInt(data['forks'].replace(',',''))
    # if row is not None :
        # changed = stars > d['stars'] or forks > d['forks']
    changed = row is not None and (stars > row[2] or forks > row[3])
    return changed



def insertDB(conn,cursor,data):
    try:
        cursor.execute('''insert into "%s" values("%s","%s",%d,%d,"%s","%s","%s")'''
        %(TAB_NAME,data['repo'],data['lang'],
        parseInt(data['stars'].replace(',','')),
        parseInt(data['forks'].replace(',','')),
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        data['repo_link'],data['desc']))
    except Exception as err:
        print err
    conn.commit()

def deleteDB(conn,cursor,repo):
    try:
        cursor.execute('''delete from "%s" where repo = "%s"''' %(TAB_NAME,repo))
    except Exception as err:
        print err
    conn.commit()

def selectDBSelf(repo):
    one = None
    conn = sqlite3.connect(keys.DB_SAVE_PATH)
    cursor = conn.cursor()
    one = selectDB(conn,cursor,repo)
    conn.close()
    return one

def selectDB(conn,cursor,repo):
    one = None
    try:
        cursor.execute('''select * from "%s" where repo = "%s"''' %(TAB_NAME,repo))
        one = cursor.fetchone()
    except Exception as err:
        print err
    conn.commit()
    return one

def parseInt(str):
    try:
        return int(str)
    except Exception as err:
        print err
        return 0
