from __future__ import print_function
import topology
from time import sleep


torus = topology.Torus(5,6)
torus.initialise()
topology.injectRandomLinkFaults(torus, 10)
torus.printTopologyMap(False)

torus.initialise()
# torus.routers[0][3].setLinkHealthList([1,0,0,0])
# torus.routers[3][0].setLinkHealthList([0,0,0,0])
topology.injectRandomRouterFaults(mesh, 4, True, 1)

mesh = topology.Mesh(26,28)
mesh.initialise()
topology.injectRandomRouterFaults(mesh, 26*27, True, 0.05)