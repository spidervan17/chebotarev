import robot
r = robot.rmap()
r.lm('task1')
r.sleep = 0.05
def task():
    r.up(1)
    r.rt(1)
    r.dn(1)
    r.rt(1)
    r.up(1)
    r.rt(1)
    r.dn(1)
r.start(task())
