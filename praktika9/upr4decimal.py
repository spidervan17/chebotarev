from decimal import Decimal
def fun(x1, x0):
    x2=Decimal(108-(815-1500/x0)/x1)
    return x2
i=int(input())
x0=Decimal(4)
x1=Decimal(4.25)
l=0
lim=fun(x1,x0)
while l<i:
    x0,x1=x1, fun(x1, x0)
    l+=1
print(x0)
while x0!=lim:
    x0,x1=x1, fun(x1, x0)
    lim=x1
print(lim)