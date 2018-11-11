class Router:
    def __init__(self, pos, linkHealthList):
        self.linkHealth = linkHealthList
        self.posx, self.posy = pos
        self.threshold = 0.03
        print("New router initialised with position [" + str(self.posx) + ", " + str(self.posy) + "]")

    def modifylinkHealth(self, direction, health):
        if(direction >= 0 and direction < 4):
            self.linkHealth[int(direction)] = health
            return True
        else:
            # print("Error: Not a valid direction")
            return False

    def getHealthyLinks(self):
        # returns an array of healthy (1) and permanent-hard-faulty (0) links
        listLink = []
        for link in self.linkHealth:
            listLink.append(1 if link > self.threshold else 0)
        return listLink

    def canTransmit(self, direction):
        # returns true if the router can be used to forward a packet in the mentioned direction
        healthyLinks = self.getHealthyLinks()
        return True if(healthyLinks[direction] == 1) else False

    def canRecieve(self, direction):
        # returns true if the packet can be used to receive a packet from the mentioned direction
        # although this looks redundant, this function is kept reserved for cases like the Router's mux fault
        healthyLinks = self.getHealthyLinks()
        return True if(healthyLinks[direction] == 1) else False

    def checkIsolated(self):
        # checks whether a router has been isolated
        return True if (self.getHealthyLinks().index(1) == -1) else False

    def checkTerminus(self):
        # checks whether the router has only one active link
        healthyLinks = self.getHealthyLinks()
        count = 0
        for link in healthyLinks:
            count = count + 1 if link == 1 else count + 0
        return True if count == 1 else False

    def route(self, source, destination):
        # returns true if the routing was successful, otherwise false
        t = True if (self.canTransmit(destination)) else False
        r = True if (self.canRecieve(source)) else False
        return [t,r]

    def selectBestLink(self, source):
        # returns direction of best transmit link
        # useful in case of local SRN
        listLink = self.linkHealth
        # get the link with highest health excluding the source
        destination = listLink.index(max(listLink.pop(source)))
        return destination

