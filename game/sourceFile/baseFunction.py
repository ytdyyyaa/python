#/usr/bin/python
#-*-coding:utf-8-*-
import random
import city
import config

def init_map(num):
    CityList = list()
    for i in num:
        start = int(random.random()*20/num)
        over = int(random.random()*20/num)
        temp = list(set(config.config.CITYNAME[start:over]))
        tempCity = city.City(config.config.CITYNAME[i],temp)
        CityList.append(tempCity)
    return CityList

def fileOp(filePath,**kw):
    pass

def showRecord():
    pass
