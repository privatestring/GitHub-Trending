#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : joker
# 用来刷新数据库，拉取最新数据

import sys,os
sys.path.append('..')
import requests,re


def searchNewInfo(row):
    try:
        url = 'https://github.com/%s' %row[2]
        response = requests.get(url)
        content = response.content
        forks = re.search('([0-9]+) users forked this repository',content).group(1)
        stars = re.search('([0-9]+) users starred this repository',content).group(1)
        desc = re.search('property="og:url" /><meta content="(.*)" property="og:description" />',content).group(1)
        repo = {}
        repo['repo'] = row[2]
        repo['lang'] = row[3]
        repo['forks'] = forks
        repo['stars'] = stars
        repo['repo_link'] = url
        repo['desc'] = desc
        return repo
    except Exception as err:
        print err
        return None

def searchNewGitInfo(row):
    try:
        url = 'https://github.com/%s' %row[0]
        response = requests.get(url)
        content = response.content
        forks = re.search('([0-9]+) users forked this repository',content).group(1)
        stars = re.search('([0-9]+) users starred this repository',content).group(1)
        desc = re.search('property="og:url" /><meta content="(.*)" property="og:description" />',content).group(1)
        repo = {}
        repo['repo'] = row[0]
        repo['lang'] = row[1]
        repo['forks'] = forks
        repo['stars'] = stars
        repo['repo_link'] = url
        repo['desc'] = desc
        return repo
    except Exception as err:
        print err
        return None
