#/usr/bin/python
#-*-coding:utf-8-*-
from __future__ import print_function
import baseFunction as bf
import hotel
import manager
import city



class Gamer(object):
    def __init__(self,name,days,citys,managers):
        self.name = name
        self.gameProfit = 0
        self.playTime = days
        self.initMangerNum = managers
        self.cityNum = citys
        self._citys = list()
        self._managers = list()

    def initTheGameData(self):
        pass

    def initTheGameMap(self):
        self._citys = bf.init_map(self.cityNum)

    def do_nothing(self):
        pass

    def move(self):
        pass

    def build(self):
        pass

    def hire(self):
        pass

    def start_game(self):
        self.initTheGameData()
        self.initTheGameMap()
        for i in self.playTime:
            sign = input("please input your OP 0 for help")
            if sign == 0:
                print("""
                    1 do nothing all day
                    2 move a manager to one city
                    3 build a new hotel in one city
                    4 hire a new manager in city where you hava on or many hotels
                """)
            elif sign == 1:
                self.do_nothing()
            elif sign == 2:
                self.move()
            elif sign == 3:
                self.build()
            elif sign == 0:
                self.hire()
            self.playTime -= 1
