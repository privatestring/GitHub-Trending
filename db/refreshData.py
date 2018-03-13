#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : joker
import sys,os
sys.path.append('..')
import requests,re,sqlite3,time
import dataManager,refreshUtils
from net import refreshNet
import keys


def refreshNewInfoCache(lang):
    refreshUtils.createDB(lang)
    newDataList = []
    conn = sqlite3.connect('/Users/joker/workSpace/db/repos.db')
    cursor = conn.cursor()
    cursor.execute('''select * from repos where language = "%s" and CAST(stargazers_count as int) > 1000 ORDER BY CAST(stargazers_count as int) DESC ''' %lang)
    rowList = cursor.fetchall()
    conn.commit()
    conn.close()
    for i in range(len(rowList)):
        print "总共有 ：%d  当前加载第：%d 条" %(len(rowList),i)
        row = rowList[i]
        result = refreshUtils.selectDBSelf(row[2],lang)
        if result is None:
            repo = refreshNet.searchNewInfo(row)
            if repo is not None:
                newDataList.append(repo)
            else:
                print 'https://github.com/%s can\'t search' %row[2]
        else:
            print row[2]+"  have been added"


        if len(newDataList) >= 10:
            refreshUtils.insertDataList(newDataList,lang)
            newDataList = []
    refreshUtils.insertDataList(newDataList,lang)

def refreshNewInfo(lang):
    newDataList = []
    conn = sqlite3.connect(keys.DB_SAVE_PATH)
    cursor = conn.cursor()
    cursor.execute('''select * from repos where lang = "%s" and stars > 500 ORDER BY stars desc''' %lang)
    rowList = cursor.fetchall()
    conn.commit()
    conn.close()
    for i in range(len(rowList)):
        print "总共有 ：%d  当前加载第：%d 条" %(len(rowList),i)
        row = rowList[i]
        repo = refreshNet.searchNewGitInfo(row)
        if repo is not None:
            newDataList.append(repo)
        else:
            print 'https://github.com/%s can\'t search' %row[0]

        if len(newDataList) >= 10:
            dataManager.manager(newDataList)
            newDataList = []
    dataManager.manager(newDataList)


def importFromGitExtraAll(lang):
    path = '/Users/joker/workSpace/db/JavaScriptCache.db'
    newDataList = []
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute('''select * from repos''')
    rowList = cursor.fetchall()
    conn.commit()
    conn.close()
    for i in range(len(rowList)):
        print "总共有 ：%d  当前加载第：%d 条" %(len(rowList),i)
        row = rowList[i]
        repo = refreshUtils.createRepo(row)
        if repo is not None:
            newDataList.append(repo)
        else:
            print 'https://github.com/%s can\'t search' %row[0]

        if len(newDataList) >= 10:
            dataManager.manager(newDataList)
            newDataList = []

    dataManager.manager(newDataList)

# 已经加入 Python,Go,HTML
def importFromExtra(lang):
    newDataList = []
    conn = sqlite3.connect('/Users/joker/workSpace/db/repos.db')
    cursor = conn.cursor()
    cursor.execute('''select * from repos where language = "%s"''' %lang)
    rowList = cursor.fetchall()
    conn.commit()
    conn.close()
    for i in range(len(rowList)):
        print "总共有 ：%d  当前加载第：%d 条" %(len(rowList),i)
        row = rowList[i]
        result = dataManager.selectDBSelf(row[2])
        if result is None:
            repo = refreshNet.searchNewInfo(row)
            if repo is not None:
                newDataList.append(repo)
            else:
                print 'https://github.com/%s can\'t search' %row[2]
        else:
            print row[2]+"  have been added"


        if len(newDataList) >= 10:
            dataManager.manager(newDataList)
            newDataList = []

    dataManager.manager(newDataList)
