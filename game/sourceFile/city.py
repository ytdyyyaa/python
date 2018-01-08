#/usr/bin/python
#-*-coding:utf-8-*-
import config

class City(object):
    def __init__(self,cityName,thisMap):
        self.name = cityName
        self.pathMap = thisMap
        self.hotelNum = list()

    #in the city add a new hotel
    def add_hotel(self,hotel):
        temp = hotel
        self.hotelNum.append(temp)

    #check the ways
    def canArrive(self,fromCity):
        for i in self.pathMap:
            if i == fromCity:
                return True
            else:
                return False