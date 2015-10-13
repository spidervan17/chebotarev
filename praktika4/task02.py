import robot
r = robot.rmap()
r.lm('task2')
r.sleep = 0.05
def zvet():
    r.rt(1)
    r.pt()
    r.rt(1)
    r.up(1)
    r.pt()
    r.up(1)
    r.lt(1)
    r.pt()
    r.lt(1)
    r.dn(1)
    r.pt()
    r.dn(1)

def test():
    r.sleep = 0.05
    for i in range(4):
        zvet()
        r.rt(3)

r.start(test)
