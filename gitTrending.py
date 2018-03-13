#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : joker
import sys
from net import requestRepos,refreshNet
from db import dataManager,loadJson,refreshData

# daily,weekly,monthly
def connectRequest():
    dataList = []
    for l in requestRepos.requestLanguage():
        result = requestRepos.requestLanguageDetail(l,'weekly')
        print "当前语言："+l
        dataManager.manager(result)
        dataList +=result
    return dataList

def printErr():
    print "============================================================================="
    print "============================可以以下命令======================================="
    print "|   python gitTrending.py search   拉取每天排行榜                             |"
    print "|   python gitTrending.py loadLocal   加载本地保存的数据                      |"
    print "|   python gitTrending.py refresh $lang 刷新数据库所有信息（量很大，适合一年一次    |"
    print "============================================================================="

def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == 'refresh':
            # refreshData.refreshNewInfo(sys.argv[2])
            # refreshData.refreshNewInfoCache(sys.argv[2])
            refreshData.importFromGitExtraAll(sys.argv[2])
        else:
            printErr()
    elif len(sys.argv) == 2:
        param = sys.argv[1]
        if param == 'search':
            connectRequest()
        elif param == 'loadLocal':
            loadJson.loadLocalJson()
        else:
            printErr()
    else:
        printErr()

if __name__ == '__main__':
    main()
