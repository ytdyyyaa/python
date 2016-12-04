#/usr/bin/python
#-*-coding:utf-8-*-

class Manager(object):
    def __init__(self):
        self.sign = 0
        self.time = 3
    def ch_sign(self):
        if self.time == 0:
            self.sign = 1
        else:
            pass

    def remainTime(self):
        if self.time == 0:
            pass
        else:
            self.time -= 1
