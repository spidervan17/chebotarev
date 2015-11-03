from fractions import Fraction
def fun(x1, x0):
    x2=Fraction(108-(815-1500/x0)/x1)
    return x2
i=int(input())
x0=Fraction(4)
x1=Fraction(4.25)
lim=fun(x1,x0)
l=0
while l<i:
    x0,x1=x1, fun(x1, x0)
    l+=1
print(float(x0))
while float(x0)!=float(lim):
    x0,x1=x1, fun(x1, x0)
    lim=x1
print(float(lim))
