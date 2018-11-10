class Router:
    def __init__(self, [posx, posy], [right, up, left, down]):
        self.linkProbability = [right, up, left, down]
        self.threshold = 0.03
        print("New router initialised with position [" + str(posx) + ", " + str(posy) + "]")

    def modifyLinkProbability(self, direction, probability):
        if(direction == 0):
            self.linkProbability[0] = probability
            return True
        elif(direction == 1):
            self.linkProbability[1] = probability
            return True
        elif(direction == 2):
            self.linkProbability[2] = probability
            return True
        elif(direction == 3):
            self.linkProbability[3] = probability
            return True
        else:
            # print("Error: Not a valid direction")
            return False

    def getHealthyLinks(self):
        # returns an array of healthy (1) and permanent-hard-faulty (0) links
        array = []
        for link in self.linkProbability:
            array.append(1 if link > threshold else 0)
        return array

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
            count = count + 1 if link == 1
        return True if count == 1 else False

    def route(self, source, destination):
        # returns true if the routing was successful, otherwise false
        t = True if (self.canTransmit(destination)) else False
        r = True if (self.canRecieve(source)) else False
        return [t,r]