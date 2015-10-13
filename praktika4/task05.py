import robot
r = robot.rmap()
r.lm('task5')
def zvet():
    r.pt()
    r.dn(1)
    r.rt(1)
    r.pt()
    r.rt(1)
    r.up(1)
    r.pt()
    r.rt(2)
def test():
    r.sleep = 0.05
    while r.fd():
        for i in range(2):
            zvet()
        r.dn(2)
        r.lt(8)
        if r.fd():
            r.dn(1)
r.start(test)
