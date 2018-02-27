import sys
import matplotlib.pyplot as plt

x = y = [1,2,3,4]

class BaseFile(object):
    def __init__(self):
    	super(BaseFile, self).__init__()
    """docstring for BaseFile"""
    def file_get_contents(self, nameFile):
        with open(nameFile, "r") as f:
            content = f.readlines()
        """in list content save data file"""
        content = [x.strip() for x in content]
        print(content)


class Tsp(object):
	"""docstring for Tsp"""
	def __init__(self):
		super(Tsp, self).__init__()
		"""on plane coordinate"""
		"""plt.ion()"""

	def drawTsp(self, x, y):
		plt.cla()
		"""scatter set point in the cordenates x,y"""
        plt.scatter(1, 1, s=100, c='k')
        """beeline with coordinate x, y"""
        plt.plot(x, y, 'r-')
        """show text in coordinate plane"""
        plt.text(-0.05, -0.05, "Total distance=%.2f" % 1, fontdict={'size': 20, 'color': 'green'})
        """draw coordinate plane with x between -0.1,4 and y -0.1,4"""
        plt.xlim((-0.1, 4))
        plt.ylim((-0.1, 4))
        plt.pause(0.01)
		

BaseFile().file_get_contents("data.txt")
Tsp().drawTsp(x, y)
"""off plane coordinate"""
""""plt.ioff()"""
plt.show()
