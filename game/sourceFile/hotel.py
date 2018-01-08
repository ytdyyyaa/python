#/usr/bin/python
#-*-coding:utf-8-*-
import config


class Hotel(object):
    def __init__(self):
        self.manager = list()
        self.work_manager = list()
        self.profit = config.config.INITPROFIT
        self._allProfit = 0


    #add a manager to this hotel
    def add_manager(self,Manager):
        if Manager.sign == 0:
            if len(self.manager) + len(self.work_manager) <3:
                self.manager.append(Manager)
        else:
            raise Exception("out of index of manager list")

    #move a manager to a new hotel
    def move_manager(self):
        if self.manager > 0:
            temp = self.manager.pop(0)
            return temp
        else:
            temp =  self.work_manager.pop(0)
            return temp

    #calculate the day profit
    def day_profit(self):
        temp = len(self.work_manager)
        self.profit = 0
        self.profit += temp * config.config.M_PROFIT
        return self.profit

    #a interface to the global scope to record the profit num
    def get_profit(self):
        return self._allProfit

    # every time must calculate a new _allProfit
    def calc_profit(self):
        self._allProfit += self.day_profit()
