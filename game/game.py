#/bin/usr/python
#-*-coding:utf-8-*-

from sourceFile import gamer
import config
from sourceFile import baseFunction as bf

gamerName =input("Please input your name")
manageNum = int(input("Please input the num of the init manager num more than 5 less than 20"))
cityNum = int(input("Please input the num of the init city num more than 5 less than 20"))
days = int(input("Please input the num of the gaming time (vitrul days) more than 5 less than 40"))

#init a new gamer
g = gamer.Gamer(gamerName,days,cityNum,manageNum)


if __name__ == '__main__':
    print """
        0 for help
        9 for record
        1 for change the Game data
        2 for start game
    """
    sign = int(input("Please input your choice"))

    if sign ==0:
        print config.config.help
    elif sign == 9:
        bf.showRecord()
    elif sign == 1:
        config.changeData()
    elif sign ==2:
        g.start_game()

