from decimal import Decimal
print('vvesti summu ipoteki')
s=float(input())
print('vvesti procent godovoy i kolvo let')
x=0.01*float(input())
y=int(input())
a=(12+x)/12
n=12*y
z=Decimal(a**(n-1)*s*(1-a)/(1-a**(n-1))).quantize(Decimal('0.01'))
d=n*z-Decimal(s)
print(z,d)
