#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : joker

import sys,os,json
sys.path.append('..')
from db import dataManager

def loadLocalJson():
    starList = []
    for name in os.listdir('./json'):
        path = os.path.join('./json',name)
        print path
        with open(path,'r') as load_f:
            load_dict = json.load(load_f)
            for data in load_dict['joker_star']:
                repo = {}
                repo['repo'] = data['lib']
                repo['lang'] = data['language']
                repo['forks'] = str(data['forks'])
                repo['stars'] = str(data['stars'])
                repo['repo_link'] = data['url']
                repo['desc'] = data['desc']
                starList.append(repo)
    for repo in starList:
        print repo['repo']

    dataManager.manager(starList)
    return starList
