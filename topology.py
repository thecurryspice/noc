from __future__ import print_function
import random
from time import sleep
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
					self.routers[i][j].setLinkHealthList([1,0,0,1])
				elif (i == self.Y-1 and j == 0):
					self.routers[i][j].setLinkHealthList([1,1,0,0])
				elif (i == 0 and j == self.X-1):
					self.routers[i][j].setLinkHealthList([0,0,1,1])
				elif (i == self.Y-1 and j == self.X-1):
					self.routers[i][j].setLinkHealthList([0,1,1,0])
				elif (i == 0 and (j > 0 and j < self.X-1)):
					self.routers[i][j].setLinkHealthList([1,0,1,1])
				elif (i == self.Y-1 and (j > 0 and j < self.X-1)):
					self.routers[i][j].setLinkHealthList([1,1,1,0])
				elif (j == 0 and (i > 0 and i < self.Y - 1)):
					self.routers[i][j].setLinkHealthList([1,1,0,1])
				elif (j == self.X-1 and (i > 0 and i < self.Y-1)):
					self.routers[i][j].setLinkHealthList([0,1,1,1])
				else:
					self.routers[i][j].setLinkHealthList([1,1,1,1])

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
						if(num == 0):
							print(" " + "---", end = "")
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
						if(num == 0):
							print(" ")
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
		for i in range(self.Y):
			for j in range(self.X):
				self.routers[i][j].setLinkHealthList([1,1,1,1])
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


# Common topology functions

def injectLinkFault(topology, pos, direction):
	X,Y = topology.getDimensions()
	j,i = pos	# position of the router
	print(j,i)
	if(j > X-1 or i > Y-1):
		print("Index out of range for given topology")
		return False
	else:
		# return true only if the link was healthy before
		if(topology.routers[i][j].getHealthyLinksList()[direction] == 1):
			topology.routers[i][j].setLinkHealth(direction, 0)
			if(direction == 0):
				topology.routers[i][wrap(j+1,0,X-1)].setLinkHealth(2,0)
			elif(direction == 1):
				topology.routers[wrap(i-1,0,Y-1)][j].setLinkHealth(3,0)
			elif(direction == 2):
				topology.routers[i][wrap(j-1,0,X-1)].setLinkHealth(0,0)
			else:
				topology.routers[wrap(i+1,0,Y-1)][j].setLinkHealth(1,0)
			return True
		else:
			print("Already a fault!")
			return False

def injectRouterFault(topology, pos):
	X,Y = topology.getDimensions()
	j,i = pos	# position of the router
	if(j > X-1 or i > Y-1):
		print("Index out of range for given topology")
		return False
	else:
		topology.routers[i][j].setLinkHealthList([0,0,0,0])
		# modify neighbours
		r, u, l, d = wrap(j+1,0,X-1), wrap(i-1,0,Y-1), wrap(j-1,0,X-1), wrap(i+1,0,Y-1) 
		topology.routers[i][l].setLinkHealth(0,0)
		topology.routers[d][j].setLinkHealth(1,0)
		topology.routers[i][r].setLinkHealth(2,0)
		topology.routers[u][j].setLinkHealth(3,0)
		
'''
Injects 'n' random faults

Works well for Torus, but not for Mesh.
The fault injection is basically a randomisation of link-healths.
Example Error: Vertex-routers in mesh 'might' get updated to 3 healthy links or 4 links
Keeping a macro for different topologies, a if-else is very simple to implement.
I'd prefer a general solution.

A workaround can be to target only healthy links and modify them, which has been implemented.
'''
def injectRandomLinkFaults(topology, n, animate=False, frameDelay=0.05):
	X,Y = topology.getDimensions()
	# a 2D planar topology will have 2*M*N links. Mesh will have M+N-2 less links.
	if n > 2*X*Y:
		print("Error: Too many elements. No faults injected.")
		return
	original = [i for i in range(X*Y)]
	for k in range(n):
		# choose a random router
		choice = random.choice(original)
		# get coordinates
		i = int(choice/X)
		j = int(choice%X)
		# choose a random link
		link = int(4*random.random())
		# check if the link is healthy
		if(topology.routers[i][j].getHealthyLinksList()[link] == 1):
			topology.routers[i][j].setLinkHealth(link, 0)
			if(link == 0):
				topology.routers[i][wrap(j+1,0,X-1)].setLinkHealth(2,0)
			elif(link == 1):
				topology.routers[wrap(i-1,0,Y-1)][j].setLinkHealth(3,0)
			elif(link == 2):
				topology.routers[i][wrap(j-1,0,X-1)].setLinkHealth(0,0)
			else:
				topology.routers[wrap(i+1,0,Y-1)][j].setLinkHealth(1,0)
			if(animate):
				topology.printTopologyMap(True)
				sleep(frameDelay)
				for c in range(2*Y):
					print("\033[F", end = '')
		else:
			try:
				injectRandomLinkFaults(topology,1)
			except RuntimeError:
				print("Maximum recursion depth reached. All links have been marked faulty.")
				topology.printTopologyMap(True)
	if(animate):
			for i in range(2*Y):
				print("\033[E", end = '')
		# [round(random.random()),round(random.random()),round(random.random()),round(random.random())]

def injectRandomRouterFaults(topology, n, animate=False, frameDelay=0.05):
	X,Y = topology.getDimensions()
	if n > X*Y:
		print("Error: Too many elements. No faults injected.")
		return
	original = [i for i in range(X*Y)]
	for k in range(n):
		# choose a random router
		choice = random.choice(original)
		# get coordinates
		i = int(choice/X)
		j = int(choice%X)
		# kill router
		topology.routers[i][j].setLinkHealthList([0,0,0,0])
		# modify neighbours
		r, u, l, d = wrap(j+1,0,X-1), wrap(i-1,0,Y-1), wrap(j-1,0,X-1), wrap(i+1,0,Y-1) 
		# print(j+1,i-1,j-1,i+1)
		# print(r, u, l, d)
		topology.routers[i][l].setLinkHealth(0,0)
		topology.routers[d][j].setLinkHealth(1,0)
		topology.routers[i][r].setLinkHealth(2,0)
		topology.routers[u][j].setLinkHealth(3,0)
		original.remove(choice)
		if(animate):
			topology.printTopologyMap(True)
			sleep(frameDelay)
			for c in range(2*Y):
				print("\033[F", end = '')
	if(animate):
		for i in range(2*Y):
			print("\033[E", end = '')

def wrap(variable, minval, maxval):
	# I should use mod here but lite for now
	if(variable < minval):
		return maxval-(minval+variable+1)
	elif(variable > maxval):
		return minval+(variable-maxval-1)
	else:
		return variable

