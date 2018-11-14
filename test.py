from __future__ import print_function
import topology
from time import sleep


torus = topology.Torus(5,6)
torus.initialise()
topology.injectRandomLinkFaults(torus, 10)
# torus.printTopologyMap(False)
# torus.initialise()
# torus.printTopologyMap(True)
# torus.routers[0][3].setLinkHealthList([1,0,0,0])
# torus.routers[3][0].setLinkHealthList([0,0,0,0])
# torus.printTopologyMap(colour = False)
# torus.printTopologyMap(colour = True)

mesh = topology.Mesh(16,16)
mesh.initialise()
topology.injectRandomRouterFaults(mesh, 254)
# mesh.initialise()
# topology.injectRandomRouterFaults(mesh,37)
mesh.printTopologyMap(False)