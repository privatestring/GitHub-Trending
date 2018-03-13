#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : joker

import sys
sys.path.append("..")
import requests,json
import keys


def requestLanguage():
    if len(keys.NEED_LANGUAGE) > 0:
        return keys.NEED_LANGUAGE
    langList = ['all']
    try:
        url = 'https://trendings.herokuapp.com/lang'
        response = requests.get(url)
        items = json.loads(response.text)['items']
        langList += items
    except Exception as err:
        print err
    return langList


def requestLanguageDetail(lang,since):
    detailList = []
    try:
        url = 'https://trendings.herokuapp.com/repo?lang=%s&since=%s' %(lang,since)
        response = requests.get(url)
        items = json.loads(response.text)['items']
        detailList += items
    except Exception as err:
        print err
    return detailList
