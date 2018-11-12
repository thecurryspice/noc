import topology

mesh = topology.Mesh(4,4)
mesh.initialise()
topology.injectRandomLinkFaults(mesh,10)
mesh.printTopologyMap(True)
mesh.initialise()
topology.injectRandomRouterFaults(mesh,10)
mesh.printTopologyMap(True)


torus = topology.Torus(5,6)
torus.initialise()
topology.injectRandomLinkFaults(torus, 10)
# torus.routers[0][3].modifyLinkHealthList([1,0,0,0])
# torus.routers[3][0].modifyLinkHealthList([0,0,0,0])
# torus.printTopologyMap(colour = False)
torus.printTopologyMap(colour = True)