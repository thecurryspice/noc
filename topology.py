from __future__ import print_function
import random
from router import *

BLUE =  '\033[1;38;2;32;64;227m'
RED =   '\033[1;38;2;227;32;32m'
GREEN = '\033[0;38;2;0;192;0m'
YELLOW ='\033[0;38;2;192;192;0m'
NC =    '\033[0m'

# Basic Mesh Topology
class Mesh:
	def __init__(self, x, y):
		self.X, self.Y = x, y
		self.routers = [[Router([i,j],[1,1,1,1]) for j in range(self.X)] for i in range(self.Y)]
		
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

	def getDimensions(self):
		return self.X, self.Y

	# prints topology in readable format
	def printTopologyMap(self, colour):
		for i in range(self.Y):
			for j in range(self.X):
				num = self.routers[i][j].getHealthyLinksCount()
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

# 2D Planar Torus topology
class Torus:
	def __init__(self, x, y):
		self.X, self.Y = x, y
		self.routers = [[Router([j,i],[1,1,1,1]) for j in range(self.X)] for i in range(self.Y)]

	# initialises the topology to with all healthy links
	def initialise(self):
		# A torus is initialised by default
		return

	def getDimensions(self):
		return self.X, self.Y

	# print topology in readable format
	def printTopologyMap(self, colour):
		for i in range(self.Y):
			for j in range(self.X):
				num = self.routers[i][j].getHealthyLinksCount()
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


'''
Injects 'n' random faults

Works well for Torus, but not for Mesh.
The fault injection is basically a randomisation of link-healths.
Example Error: Vertex-routers in mesh 'might' get updated to 3 healthy links or 4 links
Keeping a macro for different topologies, a if-else is very simple to implement.
I'd prefer a general solution.

A workaround can be to target only healthy links and modify them
'''
def injectRandomLinkFaults(topology, n):
	X,Y = topology.getDimensions()
	if n > X*Y:
		print("Error: Too many elements. No faults injected.")
		return
	selectedi, selectedj = [], []
	for k in range(n):
		i = int(Y*random.random())
		j = int(X*random.random())
		try:
			if(selectedi.index(i) == -1 and selectedj.index(j) == -1):
				k = k-1
		except:
			topology.routers[i][j].modifyLinkHealthList([round(random.random()),round(random.random()),round(random.random()),round(random.random())])
			selectedi.append(i)
			selectedj.append(j)


def injectRandomRouterFaults(topology, n):
	X,Y = topology.getDimensions()
	if n > X*Y:
		print("Error: Too many elements. No faults injected.")
		return
	selectedi, selectedj = [], []
	for k in range(n):
		i = int(Y*random.random())
		j = int(X*random.random())
		try:
			if(selectedi.index(i) == -1 and selectedj.index(j) == -1):
				k = k-1
		except:
			selectedi.append(i)
			selectedj.append(j)
			topology.routers[i][j].modifyLinkHealthList([0,0,0,0])
			r, u, l, d = wrap(j+1,0,X-1), wrap(i-1,0,Y-1), wrap(j-1,0,X-1), wrap(i+1,0,Y-1) 
			# print(j+1,i-1,j-1,i+1)
			# print(r, u, l, d)
			topology.routers[i][l].modifyLinkHealth(0,0)
			topology.routers[d][j].modifyLinkHealth(1,0)
			topology.routers[i][r].modifyLinkHealth(2,0)
			topology.routers[u][j].modifyLinkHealth(3,0)


def wrap(variable, minval, maxval):
	# I should use mod here but lite for now
	if(variable < minval):
		return maxval-(minval+variable+1)
	elif(variable > maxval):
		return minval+(variable-maxval-1)
	else:
		return variable

