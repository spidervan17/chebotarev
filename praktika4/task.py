import robot
r = robot.rmap()
r.lm('task6')
x=r.getCoordC()
y=r.getCoordR()
def zvet():
    if r.fu() and r.fd():
        r.pt()
        r.rt(1)
def test():
    r.sleep = 0.05
    r.rt(9-x)
    while r.fd() and r.fu():
        r.up(1)

    zvet()
r.start(test)
