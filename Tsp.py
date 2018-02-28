import sys
import matplotlib.pyplot as plt

coorX = [0, 0.11736202, 0.27628735, 0.28207902, 0.74977408, 0.88130897,
 0.69978883, 0.87362204, 0.32465918, 0.88724725, 0.88997274, 0.97811309,
 0.43893032, 0.48178456, 0.82098924, 0.97124457, 0.73563341, 0.65355428,
 0.70162914, 0.10381159]
coorY = [0, 0.47338678, 0.71189566, 0.81025209, 0.79890109, 0.82899792,
 0.27855368, 0.29881385, 0.14014837, 0.53078798, 0.52032261, 0.26988757,
 0.18190966, 0.26782554, 0.6227169,  0.39425376, 0.90229357, 0.42857193,
 0.22936497, 0.81217847]
x = []
y = []

class BaseFile(object):
	def __init__(self):
		super(BaseFile, self).__init__()
	"""docstring for BaseFile"""
	def file_get_contents(self, nameFile):
		content = open(nameFile)
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
					print data
					x.append(float(data[1]))
					y.append(float(data[2]))
				count+=1

class Tsp(object):
	"""docstring for Tsp"""
	def __init__(self):
		super(Tsp, self).__init__()
		self.city_position = 0
		"""on plane coordinate"""
		plt.ion()

	def drawTsp(self, x, y):
		plt.cla()
		"""scatter set point in the cordenates x,y"""
		plt.scatter(x[:], y[:], s=100, c='k')
		"""beeline with coordinate x, y"""
		plt.plot(x, y, 'r-')
		"""show text in coordinate plane"""
		plt.text(-0.05, -0.05, "Total distance=%.2f" % 1, fontdict={'size': 14, 'color': 'green'})
		"""draw coordinate plane with x between -0.1,4 and y -0.1,4"""
		plt.xlim((-max(x)/10, max(x)+(max(x)/10)))
		plt.ylim((-max(x)/10, max(y)+(max(x)/10)))
		plt.pause(0.01)

	def buildRoute(self, coorX, coorY):
		Tsp().drawTsp(coorX, coorY)
		
	def nearestNeighbors(self):
		self

BaseFile().file_get_contents("berlin52.tsp")
Tsp().buildRoute(x, y)
"""off plane coordinate"""
plt.ioff()
plt.show()
