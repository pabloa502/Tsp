import matplotlib.pyplot as plt
import math as m
import numpy as np
import sys

class BaseFile(object):
	def __init__(self):
		super(BaseFile, self).__init__()
	"""docstring for BaseFile"""
	def getContent(self, nameFile):
		content = open(nameFile)
		coor = []
		print content.readline()
		print content.readline()
		print content.readline()
		dimension = content.readline().split(" ")[1]
		print dimension
		print content.readline()
		print content.readline()
		count = 1
		with content as fp:
			for line in fp:
				if count <= int(dimension):
					data = line.split(" ")
					coor.append([float(data[1]), float(data[2])])
				count+=1
		print coor
		return coor

class Tsp(object):
	"""docstring for Tsp"""
	def __init__(self):
		super(Tsp, self).__init__()
		"""on plane coordinate"""
		plt.ion()

	def drawTsp(self, x, y, dt):
		plt.cla()
		"""scatter set point in the cordenates x,y"""
		plt.scatter(x[:], y[:], s=100, c='k')
		"""beeline with coordinate x, y"""
		plt.plot(x, y, 'r-')
		"""show text in coordinate plane"""
		plt.text(-max(x)/10, -max(x)/10, "Total distance=%.2f" % dt, fontdict={'size': 12, 'color': 'green'})
		"""draw coordinate plane with x between -0.1,4 and y -0.1,4"""
		plt.xlim((-max(x)/10, max(x)+(max(x)/10)))
		plt.ylim((-max(x)/10, max(y)+(max(x)/10)))
		plt.pause(0.01)

	def buildRoute(self):
		coorR = [coor.pop(0)]
		dt = 0
		while coor:
			d, p2 = self.nearestNeighbors(coorR[-1])
			dt += d
			coorR.append(p2)
		coorR.append(coorR[0])
		coorR = np.array(coorR)
		self.drawTsp(coorR[:,0], coorR[:,1], dt)
		
	def nearestNeighbors(self, p1):
		d = -1
		pos = -1
		i = 0
		for item in coor[:]:
			dTemp = self.getDistance(p1, item)
			if d == -1 or dTemp < d:
				d = dTemp
				pos = i
			i += 1

		return d, coor.pop(pos)

	def getDistance(self, p1, p2):
		return m.hypot(p2[0] - p1[0], p2[1] - p1[1])

nameFile = "data/" + sys.argv[1]
coor = BaseFile().getContent(nameFile)
Tsp().buildRoute()
"""off plane coordinate"""
plt.ioff()
plt.show()
