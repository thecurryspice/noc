from router import *
r00 = Router([0,0],[1,1,1,1])
r01 = Router([0,1],[1,1,1,1])
r02 = Router([0,2],[1,1,1,1])
r10 = Router([1,0],[1,1,1,1])
r11 = Router([1,1],[1,1,1,1])
r12 = Router([1,2],[1,1,1,1])
r20 = Router([2,0],[1,1,1,1])
r21 = Router([2,1],[1,1,1,1])
r22 = Router([2,2],[1,1,1,1])

print(r22.canTransmit(3))