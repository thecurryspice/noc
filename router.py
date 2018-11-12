class Router:
    def __init__(self, pos, linkHealthList):
        self.linkHealth = linkHealthList
        self.posx, self.posy = pos
        self.threshold = 0.03
        # print("New router initialised with position [" + str(self.posx) + ", " + str(self.posy) + "]")

    # modifies health for one specific link
    def modifyLinkHealth(self, direction, health):
        if(abs(direction) < 4):
            self.linkHealth[int(direction)] = health
            return True
        else:
            # print("Error: Not a valid direction")
            return False

    # modify health list
    def modifyLinkHealthList(self, linkHealthList):
        if(abs(len(linkHealthList) == 4)):
            self.linkHealth = linkHealthList
            return True
        else:
            # print("Error: Unexpected length")
            return False

    # returns an array of healthy (1) and permanent-hard-faulty (0) links
    def getHealthyLinksList(self):
        listLink = []
        for link in self.linkHealth:
            listLink.append(1 if link > self.threshold else 0)
        return listLink

    def getHealthyLinksCount(self):
        count = 0
        for link in self.getHealthyLinksList():
            count = count +1 if link == 1 else count
        return count

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
    def checkIsolated(self):
        return True if (self.getHealthyLinksList().index(1) == -1) else False
    
    # checks whether the router has only one active link
    def checkTerminus(self):
        count = self.getHealthyLinksCount()
        return True if count == 1 else False

    # returns direction of best transmit link
    # useful in case of local SRN
    def selectBestLink(self, source):
        listLink = self.linkHealth
        # get the link with highest health excluding the source
        destination = listLink.index(max(listLink.pop(source)))
        return destination