#-*-coding:utf-8-*-

class intNum(object):
	def __init__(self,num):
		self.num = num
	def get(self):
		return self.num


if __name__ == "__main__":
	li = list()
	for i in range(0,10):
		temp = intNum(i)
		li.append(temp)

	for j in range(0,10):
		print li[j].get()