class Router:
    def __init__(self, pos, linkHealthList):
        self.linkHealth = linkHealthList
        self.posx, self.posy = pos
        self.threshold = 0.03
        self.cost = self.heuristic = 0
        self.parent = None
        self.weight = 1
        self.linkWeightList = [1,1,1,1]
        # print("New router initialised with position [" + str(self.posx) + ", " + str(self.posy) + "]")

    # modifies health for one specific link
    def setLinkHealth(self, direction, health):
        if(abs(direction) < 4):
            self.linkHealth[int(direction)] = health
            return True
        else:
            # print("Error: Not a valid direction")
            return False

    # modify health list
    def setLinkHealthList(self, linkHealthList):
        if(abs(len(linkHealthList) == 4)):
            self.linkHealth = linkHealthList
            return True
        else:
            # print("Error: Unexpected length")
            return False

    # sets cost and heursitic values stored in the router
    def setCostHeuristic(self, **kwargs):
        try:
            self.cost = kwargs['cost']
        except:
            pass
        try:
            self.heuristic = kwargs['heuristic']
        except:
            pass

    # sets router weight
    def setWeight(self, weight):
        self.weight = weight

    # sets the link weight
    def setLinkWeight(self, direction, weight):
        self.linkWeightList[direction] = weight

    # returns X,Y position, useful for routing packets around
    def getPosition(self):
        return self.posx, self.posy

    # returns an array of healthy (1) and permanent-hard-faulty (0) links
    def getHealthyLinksList(self):
        listLink = []
        for link in self.linkHealth:
            listLink.append(1 if link > self.threshold else 0)
        return listLink

    # returns number of healthy links based on threshold
    def getHealthyLinksCount(self):
        count = 0
        for link in self.getHealthyLinksList():
            count = count +1 if link == 1 else count
        return count

    # returns the total cost
    # The reason that cost and heuristic are used instead of one varibale is because
    # some algorithms do not implement the heuristic function, in which case
    # only Cost function can be used.
    def getCost(self):
        return (self.weight*(self.cost + self.heuristic))

    # returns router weight
    def getWeight(self):
        return self.weight

    # returns the link weight
    def getLinkWeight(self, direction):
        return self.linkWeightList[direction]

    # returns a tuple of cost and heuristic values
    def getCostHeuristic(self):
        return (self.weight*self.cost, self.weight*self.heuristic)

    # returns true if the router can be used to forward a packet in the mentioned direction
    def canTransmit(self, direction):
        healthyLinks = self.getHealthyLinksList()
        return True if(healthyLinks[direction] == 1) else False

    # returns true if the packet can be used to receive a packet from the mentioned direction
    # although this looks redundant, this function is kept reserved for cases like the Router's mux fault    
    def canReceive(self, direction):
        healthyLinks = self.getHealthyLinksList()
        return True if(healthyLinks[direction] == 1) else False
    
    # returns true if the routing was successful, otherwise false
    def route(self, source, destination):
        t = True if (self.canTransmit(destination)) else False
        r = True if (self.canRecieve(source)) else False
        return [r,t]
    
    # checks whether a router has been isolated
    def isIsolated(self):
        return True if (self.getHealthyLinksCount() == 0) else False
    
    # checks whether the router has only one active link
    def isTerminus(self):
        count = self.getHealthyLinksCount()
        return True if count == 1 else False

    # returns direction of best transmit link
    # useful in case of local SRN
    def selectBestLink(self, source):
        listLink = self.linkHealth
        # get the link with highest health excluding the source
        destination = listLink.index(max(listLink.pop(source)))
        return destination

def wrap(variable, minval, maxval):
    # I should use mod here but lite for now
    if(variable < minval):
        return maxval-(minval+variable+1)
    elif(variable > maxval):
        return minval+(variable-maxval-1)
    else:
        return variable