# NOC (Network On Chips)

This repository contains classes/modules that ease implementation and testing of NOC algorithms on varying topologies.<br>
This work is done in the hope that it is found useful by scholars working in this domain. 

`test.py` is a sample program and can be used as a quick-start.

---

# Topology

API Documentation for all the classes is yet to be made. Appropriate comments have been made in individual class/files for the programmer's comprehension.

## Invoking A Topology

Invoke a topology map with<br>
`topo = topology.Topology(M,N)`<br>
where 'Topology' can be either *Mesh* or *Torus* with **M** and **N** as horizontal and vertical dimensions.<br>
Invoking a topology only creates relevant (router/link/packet) objects. The topology has to be initialised before it starts behaving properly.

## Initialisation

The topology has to be initialised so that the individual router elements can be linked properly to each other. This also works as a 'reset' for when all connections have to be restored to a healthy state.<br>
`topo.initialise()` initialises the topology.<br>

Once the topology is initialised, the routers can be accessed as elements of a 2D matrix.<br>
`print(topo.routers)`

A nicer and more human-readable view can be obtained on the console using<br>
`topo.printTopologyMap(colour)`<br>
Setting `colour` to `True` outputs faulty routers in Red and terminal routers in Yellow. Setting it to `False` outputs faulty routers as empty spaces.

## Indexing

All routers forming the topology can be accessed using column and row indices using:<br>
`topo.routers[y][x]`<br>
Notice that the first index corresponds to the **y**th row and the second index to the **x**th column. This indexing is indeed, different from the conventional (x,y) addressing in graphs.<br>
However, the module maintains this convention (x,y) when accepting position as a parameter or returning position as a tuple.<br>
As stated, the only exception to this is when accessing routers directly.

## Path Finding

The module consists of a path-finding functionality that can be accessed using<br>
`findPath(topology, source, destination)`, which returns the first-hit shortest path between two nodes using a modified A* approach.
The parameters `source` and `destination` are not positions but `Router` objects. This has been done to improve readability.<br>
Each topology contains a heuristic function that determine the path-finding behaviour. Custom topologies need to include this heuristic to make use of this functionality.

`showPath(topology, path)` prints the map in a nice graphical view on a terminal console, with the path highlighted in Green.

## Fault Injection

Router or Link faults can be injected easily either by targeting individual routers/links or generating *n* random faults.<br>

### Individual Targeting

`topo.routers[2][1].setLinkHealthList([1,1,0,1])`<br>

Here, the function parameter is a list of links' healths in the order right([0]), up([1]), left([2]), down([3]).<br>
`[1,1,0,1]` means that the *left link* has been marked as a permanent fault.<br>
`[0,0,0,0]` would mean that the router is set as faulty.


`topo.routers[2][1].setLinkHealth(0,0.4)`<br>

Here, the function parameters are (direction,linkHealth).<br>
`[0,0.4]` means that the link pointing to the right of the router indexed at X=1, Y=2 has a health of 0.4 (out of 1).

### Random Fault Generation

The topology class contains direct functions for generating 'N' random faults using<br>
`topology.injectRandomLinkFaults(topo, N, animate = True, frameDelay = 0.5)` or
`topology.injectRandomRouterFaults(topo, N, animate = True, frameDelay = 0.5)`

`animate` and `frameDelay` are optional arguments and allow for visualising a slow injection of faults. This is not just an aesthetic addition, it also helps to see how the topology evolves with random injections, which can be very insightful for large maps with stochastically placed links. The variable names are obvious enough for defining their purpose.

---

# Router

Once the router has been accessed as an element in a 2D matrix, all functions related to packet-traversal can be used to simulate handling an actual packet.<br>
As of now, the Packet object is not accepted in any of Router's functions. Simulations can still be done the usual way using `canTransmit()`, `canReceive()`, and `route()`.<br>

---

# To-Do

* Implement a Packet object for routing around the topology with
	* header, body, and tail flits/segments
	* virtual stack for path debugging
	* real header data stack
	* various metrics like hop-count, latency, etc.
* Support for arbitrary number of links for each router to extend support for MoT or BFT
* Integrate Packet with traversal in the Router function-parameters
* Add FIFO buffer to router and consider Packet's size in the FIFO
* Print links in topology map according to link-health