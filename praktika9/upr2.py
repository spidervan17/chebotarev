def fun(x1, x0):
    x2=108-(815-1500/x0)/x1
    return x2
i=int(input())
x0=4
x1=4.25
l=0
while l<i:
    #if l==11:
     ##   x1+=0.03
    x0,x1=x1, fun(x1, x0)
    l+=1
    print(x0)