#-*-coding:utf-8-*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import structs as s
import random as r
from models import ServicePerson as sp
import json
# Create your views here.

class waitInLine():
    __NowList = []
    __CanService = True
    __NowNum = 0
    __InLine = 0

    def ChangeServiceStatus(self):
        return not self.__CanService

    def AddPersonInLine(self):
        self.__NowList.append(s.person(self.__NowNum + 1," "+r.randint(0,1000000)))
        self.__NowNum += 1
        self.__InLine += 1

    def SaveInDB(self,li):
        Complete = li.pop()
        try:
            u = sp(Pid = Complete.Num,Ppass = Complete.Pass)
            u.save()
        except Exception:
            return False
        return True

    def Admin(self,request):
        dict = {}
        dict['UserInfo'] = self.__NowList[1:]
        dict['WaitNum'] = self.__NowNum - 1
        dict['NowPass'] = self.__NowList[0].Pass
        dict['NowNum'] = self.__NowList[0].Num
        return render_to_response('admin.html',dict)

    def GetIndex(self,rquest):
        return render_to_response('index.html',{'PersonInWaitLine':self.__NowNum-1})

    def Called(self,request):
        if self.__CanService:
            dict = {}
            dict['GetStatus'] = True
            dict['Reason'] = ""
            dict['NowNum'] = self.__NowList[len(self.__NowList)-1].Num
            dict['NowPass'] = self.__NowList[len(self.__NowList)-1].Pass
            return render_to_response('called.html',dict)
        else:
            dict = {}
            dict['GetStatus'] = False
            dict['Reason'] = "Some things wrong!"
            return render_to_response('called.html', dict)

    def GetNext(self,request,nowNum):
        self.SaveInDB(self.__NowList)
        self.__NowNum -= 1
        dict = {}
        dict['pass'] = self.__NowList[0].Pass
        dict['num'] = self.__NowList[0].Num
        dict['WaitNum'] = self.__NowNum
        dict['arr'] = self.__NowList[nowNum-1:]
        res = json.dumps(dict)
        return HttpResponse(request,res)

    def ToZero(self,request):
        self.__NowList = []
        return HttpResponse(request,"")

    def Suspend(self,request):
        self.ChangeServiceStatus()
        return HttpResponse(request,'Success!')



