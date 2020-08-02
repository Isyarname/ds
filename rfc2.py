from random import randint, choice
from math import log2

def GenDataSet(n=10):
	data = []
	for i in range(n):
		data.append(randint(0, 2))
	return(data)

def Probability(submultitudeSize, multitudeSize):
	return submultitudeSize/multitudeSize

def SEntropy(probability: list):
	try:
		S = 0
		for i in probability:
			S -= i * log2(i)
	except ValueError:
		S = 0
	return S

def Split(data: list):
	p = randint(1 , len(data)-1)
	L1 = data[:p]
	L2 = data[p:]
	return [L1, L2]

def Counter(data: list):
	m = {}
	for i in data:
		if i in m.keys():
			m[i] += 1
		else:
			m[i] = 1 
	return m

def abgyosh(data: list, lvl=0):
	if len(tree)-1 < lvl:
		tree.append([])
	tree[lvl].append(data)
	c = Counter(data)
	pr = []
	for i in c.values():
		pr.append(Probability(i, len(data)))
	s = SEntropy(pr)
	if s == 0:
		bl.append(data)
	else:
		sd = Split(data)
		for i in sd:
			abgyosh(i, lvl + 1)

def Grouper(data: list):
	m = {}
	for i in data:
		key = str(i[0])
		if key in m.keys():
			m[key].extend(i)
		else:
			m[key] = i
	return m

ds = GenDataSet(randint(10, 15))
bl = [] 							# Список со однородными списками
tree = [] 							# Список для правильного вывода дерева
abgyosh(ds)
for i in tree:
	print(i)
sl = Grouper(bl)
print(sl)