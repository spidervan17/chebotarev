def fun(x0, x1):
    x2=108-(815-1500/x1)/x0
    return x2
x0=4
x1=4.25
lim=fun(x1,x0)
while x0!=lim:
    x0,x1=x1, fun(x1, x0)
    lim=x1
print(lim)