from __future__ import print_function
import simvar
import topology
from time import sleep


torus = topology.Torus(10,10)
torus.initialise()
for router in simvar.faultyRouters:
	topology.injectRouterFault(torus,router)
# topology.injectRandomLinkFaults(torus, 600)
# topology.injectRandomLinkFaults(torus, 200, True, 0.01)
# topology.printTopologyMap(torus, True)
# sleep(1)
# torus.routers[1][1].setLinkHealthList([1,1,1,1])
# torus.routers[17][36].setLinkHealthList([1,1,1,1])
source = torus.routers[simvar.source[0]][simvar.source[1]]
destination = torus.routers[simvar.destination[0]][simvar.destination[1]]
# fetch path
path = topology.findPath(torus,source,destination)

print("Tracing path from {0}-->{1}".format(source.getPosition(),destination.getPosition()))
print(path)
# display the path
topology.showPath(torus,path)