import random

class Matrix:
	def __init__(self, width=0, height=0, homogeneous=False, value=7, ls=[]):
		self.body = []
		self.maxValLen = len(str(value))
		if len(ls) == 0:
			if homogeneous == True:
				for i in range(height):
					temp = []
					for j in range(width):
						temp.append(value)
					self.body.append(temp)
			else:
				n = 0
				for i in range(height):
					temp = []
					for j in range(width):
						n += 1
						temp.append(n)
					self.body.append(temp)
				self.maxValLen = len(str(n))
		else:
			self.body.extend(ls)
			if type(ls[0]) == int:
				for i in ls:
					lenght = len(str(i))
					if lenght > self.maxValLen:
						self.maxValLen = lenght
			else:	
				for i in ls:
					for j in i:
						lenght = len(str(j))
						if lenght > self.maxValLen:
							self.maxValLen = lenght

	def matrixToString(self):
		s = ""
		if type(self.body[0]) != int:
			for i, o in enumerate(self.body):
				for j, oo in enumerate(o):
					val = str(oo)
					s += val + " "
					if len(val) < self.maxValLen:
						for i in range(self.maxValLen - len(val)):
							s += " "
				s += "\n"
		else:
			for i in self.body:
				s += str(i) + " "
		return s

	def transpose(self):
		ls = []
		if type(self.body[0]) != int:
			for i in range(len(self.body[0])):
				ls.append([])

			for i in self.body:
				for j in range(len(i)):
					ls[j].append(i[j])
			self.body = ls
		else:
			print("одномерный список не подходит")

	def fill(self, value):
		if type(self.body[0]) == int:
			for i in range(len(self.body)):
				self.body[i] = value
		else:
			for i in range(len(self.body)):
				for j in range(len(self.body[i])):
					self.body[i][j] = value

	def flatten(self):
		ls = []
		for i in range(len(self.body)):
			ls.extend(self.body[i])
		self.body = ls

	def shuffle(self):
		lenX = len(self.body)
		lenY = len(self.body[0])
		if type(self.body[0]) == int:
			random.shuffle(self.body)
		else:
			for i in range(lenX):
				for j in range(lenY):
					x = random.randint(0, lenX-1)
					y = random.randint(0, lenY-1)
					self.body[i][j], self.body[x][y] = self.body[x][y], self.body[i][j]		

	def reshape(self, width, height):
		if type(self.body[0]) == int:
			lenght = len(self.body)
		else:
			lenght = len(self.body) * len(self.body[0])

		if width*height != lenght:
			print("неподходящий размер матрицы")
		else:
			if type(self.body[0]) != int:
				self.flatten()
			ls = []
			n = 0
			for i in range(height):
				ls.append([])
				for j in range(width):
					if n < lenght:
						ls[i].append(self.body[n])
						n += 1
					else:
						break
			self.body = ls

	def copy(self):
		return self.body

	def __str__(self):
		return self.matrixToString()

	def __add__(self, other):
		for i,o in enumerate(self.body):
			for j,oo in enumerate(o):
				self.body[i][j] = oo + other
		return Matrix(ls=self.body)

	def __radd__(self, other):
		for i,o in enumerate(self.body):
			for j,oo in enumerate(o):
				self.body[i][j] = other + oo
		return Matrix(ls=self.body)

	def __sub__(self, other):
		for i,o in enumerate(self.body):
			for j,oo in enumerate(o):
				self.body[i][j] = oo - other
		return Matrix(ls=self.body)

	def __rsub__(self, other):
		for i,o in enumerate(self.body):
			for j,oo in enumerate(o):
				self.body[i][j] = other - oo
		return Matrix(ls=self.body)


def concantenate(t, axis=0):
	ls = []
	if axis == 0:
		for i in t:
			ls.extend(i.body)

	elif axis == 1:
		for i in range(len(t[0].body)):
			ls.append([])

		for i in range(len(t[0].body)):
			for j in t:
				ls[i].extend(j.body[i])
	return Matrix(ls=ls)

a = Matrix(5,6)
print(a)
b = a.copy()
c = Matrix(ls=b)
c.reshape(6,5)
print(c)

'''test1 = Matrix(ls=[[1,2], [3,4], [5,6]])
test2 = Matrix(ls=[[7,8], [9,10], [11,12]])
test3 = Matrix(ls=[[13,14], [15,16], [17,18]])
res = concantenate((test1, test2, test3), axis=1)
print(res)'''