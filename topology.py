from __future__ import print_function
from router import *

BLUE =  '\033[1;38;2;32;64;227m'
RED =   '\033[1;38;2;227;32;32m'
GREEN = '\033[0;38;2;0;192;0m'
YELLOW ='\033[0;38;2;192;192;0m'
NC =    '\033[0m'

class Mesh:
	def __init__(self, x, y):
		self.X, self.Y = x, y
		self.routers = [[Router([j,i],[1,1,1,1]) for j in range(self.X)] for i in range(self.Y)]
		
	# initialises the topology to with all healthy links
	def initialise(self):
		for i in range(self.Y):
			for j in range(self.X):
				if(i == 0 and j == 0):
					self.routers[i][j].modifyLinkHealthList([1,0,0,1])
				elif (i == self.Y-1 and j == 0):
					self.routers[i][j].modifyLinkHealthList([1,1,0,0])
				elif (i == 0 and j == self.X-1):
					self.routers[i][j].modifyLinkHealthList([0,0,1,1])
				elif (i == self.Y-1 and j == self.X-1):
					self.routers[i][j].modifyLinkHealthList([0,1,1,0])
				elif (i == 0 and (j > 0 and j < self.X-1)):
					self.routers[i][j].modifyLinkHealthList([1,0,1,1])
				elif (i == self.Y-1 and (j > 0 and j < self.X - 1)):
					self.routers[i][j].modifyLinkHealthList([0,1,1,1])
				elif (j == 0 and (i > 0 and i < self.Y - 1)):
					self.routers[i][j].modifyLinkHealthList([1,1,0,1])
				elif (j == self.X-1 and (i > 0 and i < self.Y - 1)):
					self.routers[i][j].modifyLinkHealthList([1,1,1,0])
				else:
					pass

	# prints topology in readable format
	def printTopologyMap(self, colour):
		for i in range(self.Y):
			for j in range(self.X):
				num = self.routers[j][i].getHealthyLinksCount()
				if(j < self.X-1):
					if colour:
						if(num == 0):
							print(RED + str(num) + NC + "---", end = "")
						elif(num == 1):
							print(YELLOW + str(num) + NC + "---", end = "")
						else:
							print(str(num) + "---", end = "")
					else:
						print(str(num) + "---", end = "")
				else:
					if colour:
						if(num == 0):
							print(RED + str(num) + NC)
						elif(num == 1):
							print(YELLOW + str(num) + NC)
						else:
							print(str(num))
					else:
							print(str(num))
			for j in range(self.X):
				if(i != self.Y - 1):
					print("|", end = "   ")
			print()



class Torus:
	def __init__(self, x, y):
		self.X, self.Y = x, y
		self.routers = [[Router([j,i],[1,1,1,1]) for j in range(self.X)] for i in range(self.Y)]

	# initialises the topology to with all healthy links
	def initialise(self):
		# A torus is initialised by default
		return

	def printTopologyMap(self, colour):
		for i in range(self.Y):
			for j in range(self.X):
				num = self.routers[j][i].getHealthyLinksCount()
				if(j < self.X-1):
					if colour:
						if(num == 0):
							print(RED + str(num) + NC + "---", end = "")
						elif(num == 1):
							print(YELLOW + str(num) + NC + "---", end = "")
						else:
							print(str(num) + "---", end = "")
					else:
						print(str(num) + "---", end = "")
				else:
					if colour:
						if(num == 0):
							print(RED + str(num) + NC)
						elif(num == 1):
							print(YELLOW + str(num) + NC)
						else:
							print(num)
					else:
						print(num)
			for j in range(self.X):
				if(i != self.Y-1):
					print("|", end = "   ")
			print()

mesh = Mesh(4,4)
mesh.initialise()
mesh.printTopologyMap()

torus = Torus(4,4)
torus.routers[0][3].modifyLinkHealthList([1,0,0,0])
torus.routers[3][0].modifyLinkHealthList([0,0,0,0])
torus.printTopologyMap(colour = False)
torus.printTopologyMap(colour = True)