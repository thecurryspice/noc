from __future__ import print_function
import topology
from time import sleep
import pdb

# create a 2D grid of required size
mesh = topology.Mesh(10,10)
# initialise all connections
mesh.initialise()
# inject some random faults
topology.injectRandomLinkFaults(mesh, 10)
topology.injectRandomRouterFaults(mesh, 6)
# view the map health
mesh.printTopologyMap(True)

'''
Working:
The algorithm follows a recursive approach, while keeping track of 3 global variables:
1. Index of routers already visited
2. Minimum hop-count
3. Corresponding stack (path)

The source is marked visited and neighbours are fetched.
1. Start with Source
2. If All links 0 == no path
3. Mark current router as visited; add 1 to hop count; update stack-trace
4. Get active neighbours
5. Check whether an active neighbour is destination.
6. If No, return True if at least one neighbour exists else return False; if Yes, go to 8
7. go to statement 2
8. Get hop-count and stack-trace.

'''

# define source and destination routers, note that
# router at (x,y) is accessed by routers[y][x]
source = mesh.routers[0][0]
destination = mesh.routers[9][8]
# fetch path
path = topology.findPath(mesh,source,destination)

print("Tracing path from {0}-->{1}".format(source.getPosition(),destination.getPosition()))
# display the path
mesh.showPath(path)