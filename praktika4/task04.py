import robot
r = robot.rmap()
r.lm('task4')
def zvet():
    r.dn(1)
    for i in range(3):
        r.pt()
        r.dn(2)
    r.dn(1)
    r.lt(1)
    for i in range(3):
        r.up(2)
        r.pt()
    r.lt(1)

def test():
    r.sleep = 0.05
    x=r.getCoordC()
    y=r.getCoordR()
    r.rt(6-x)
    r.up(y-1)
    for i in range(2):
        zvet()
    r.dn(1)
    for i in range(2):
        r.pt()
        r.dn(2)
    r.pt()
r.start(test)
