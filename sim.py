from __future__ import print_function
import simvar
import topology
from time import sleep
import pdb
import argparse

torus = topology.Torus(4,4)
torus.initialise()

# simvar.faultyLinks contains random faults for a 20x30 grid
# Parts of these faults can be loaded into any topology by plugging the faults in try-except
# for router in simvar.faultyRouters:
# 	topology.injectRouterFault(torus,router)

# simvar.faultyLinks contains random faults for a 20x30 grid
# Parts of these faults can be loaded into any topology by plugging the faults in try-except
# for fault in simvar.faultyLinks:
# 	try:
# 		topology.injectLinkFault(torus, fault[0], fault[1])
# 	except:
# 		pass

# optionally inject any random link faults if necessary
# faults = topology.injectRandomLinkFaults(torus, 6)
# print(faults)

# print the map once
# topology.injectRandomLinkFaults(torus, 4)
topology.printTopologyMap(torus, True)

# set source and destination as per simvar file
for edge in simvar.edges:
	source = torus.routers[edge[0][1]][edge[0][0]]
	destination = torus.routers[edge[1][1]][edge[1][0]]

	print("Tracing path from {0}-->{1}".format(source.getPosition(),destination.getPosition()))
	# fetch path metrics, simple as that :)
	path, pathCost = topology.findPath(torus,source,destination,1.2)
	# optionally display the path
	topology.showPath(torus,path)
	print("Path cost: {0}\nPath: {1}".format(pathCost, path))
	torus.clearPathInfo()