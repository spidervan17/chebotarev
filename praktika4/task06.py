import robot
r = robot.rmap()
r.lm('task6')
verh=int(input())
palka=int(input())
def zvet():
    for i in range(verh):
        r.pt()
        r.rt(1)
    r.lt(palka//2+1)
    for i in range(palka):
       r.pt()
       r.dn(1)
def test():
    r.sleep = 0.05
    zvet()
r.start(test)
