import matplotlib.pyplot as plt
import math as m
import numpy as np
import copy as cp
import sys
import datetime as dt

from anytree import Node, RenderTree  

class TspNode(Node):
	#docstring for BaseFile#
	separator = "->"
	coor = None
	d = 0

class BaseFile(object):
	#docstring for BaseFile#
	def __init__(self):
		super(BaseFile, self).__init__()

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
		return coor

class Tsp(object):
	#docstring for Tsp#
	def __init__(self, breadth, depth, pilot):
		self.breadth = breadth
		self.depth = depth
		self.pilot = pilot
		self.coorR = []
		self.d = 0
		#on plane coordinate#
		plt.ion()

	def drawTsp(self, x, y, dt):
		plt.cla()
		#scatter set point in the cordenates x,y#
		plt.scatter(x[:], y[:], s=100, c='k')
		#beeline with coordinate x, y#
		plt.plot(x, y, 'r-')
		#show text in coordinate plane#
		plt.text(-max(x)/10, -max(x)/10, "Total distance=%.2f" % dt, fontdict={'size': 12, 'color': 'green'})
		#draw coordinate plane with x between -0.1,4 and y -0.1,4#
		plt.xlim((-max(x)/10, max(x)+(max(x)/10)))
		plt.ylim((-max(x)/10, max(y)+(max(x)/10)))
		plt.pause(0.01)

	def buildRoute(self, coor):
		#print date init#
		print "init date: " + str(dt.datetime.now())
		#create root node #
		coorBase = TspNode(coor.pop(0))
		#copy coodenates #
		coorBase.coor = cp.copy(coor)
		#build pilot with temporal node for finished path#
		self.buildPilot(coorBase, self.pilot)
		#added initial position#
		self.coorR.append(self.coorR[0])
		#transform coordinates to print#
		self.coorR = np.array(self.coorR)
		self.drawTsp(self.coorR[:,0], self.coorR[:,1], self.d)
		#print date end#
		print "end date: " + str(dt.datetime.now())
		#print graph#
		for pre, fill, node in RenderTree(coorBase):
			print("%scoordinate:%s-distance:%s" % (pre, node.name, node.d))

	def buildPilot(self, root, pilot):
		root.children = []
		#case when it used pilot method#
		if pilot > 0:
			root.children = self.addChild(root, self.breadth)
			pilot -=1
		#case when it used temporal prediction method#
		else:
			#build temporal tree#
			root.children = self.addChild(root, 1)
		#if exist coordenates#
		if root.children:
			for child in root.children:
				self.buildPilot(child, pilot)
		#when the construction of the route is completed#
		else:
			#save the better route#
			if self.d == 0 or self.d > root.d:
				self.d = root.d
				while root:
					self.coorR.insert(0,root.name)
					root = root.parent

	def addChild(self, parent, breadth):
		children = []
		newCoor = cp.copy(parent.coor)
		if parent.coor:
			for i in range(breadth):
				d, child = self.nearestNeighbors(newCoor, parent.name)
				newNode = TspNode(child)
				#create child with distance and coordenate#
				childCoor = cp.copy(parent.coor)
				childCoor.remove(child)
				newNode.coor = childCoor
				newNode.d += d + parent.d
				
				children.append(newNode)
		return children
		
	def nearestNeighbors(self, coor, p1):
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

nameFile = "data/berlin52.tsp"
breadth = 2
depth = 3
pilot = 1

if len(sys.argv) > 1:
	nameFile = "data/" + sys.argv[1]
coor = BaseFile().getContent(nameFile)
# optional parameter breadth, depth, pilot

if len(sys.argv) > 2:
	breadth = int(sys.argv[2])
if len(sys.argv) > 3:
	depth = int(sys.argv[3])
if len(sys.argv) > 4:
	pilot = int(sys.argv[4])
Tsp(breadth, depth, pilot).buildRoute(coor)
#off plane coordinate#
plt.ioff()
plt.show()