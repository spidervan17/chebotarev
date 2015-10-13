import robot
r = robot.rmap()
r.lm('task3')
def zvet():
    if r.fd():
        r.dn(1)
        r.up(1)
        r.rt(1)
    else:
        r.rt(1)

def test():
    r.sleep = 0.05
    r.rt(1)
    for i in range(6):
        zvet()
    r.rt(1)
r.start(test)
