
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
print('vvesti summu ipoteki')
s=float(input())
print('vvesti procent godovoy i kolvo let')
x=0.01*float(input())
y=int(input())
a=(12+x)/12
n=12*y
z=Decimal(a**(n-1)*s*(1-a)/(1-a**(n-1))).quantize(Decimal('0.01'))

t = np.arange(0., n, 0.2)
#Остаток
plt.subplot(221)
plt.plot(t,(Decimal(s*(a**t))-Decimal((a**t-1)/(a-1))*z),'r--')
plt.title(r'Остаток по кредитам')
plt.grid(True)
#Выплаты
plt.subplot(222)
plt.plot(t,(Decimal(1-a))*(Decimal(s*(a**t))-Decimal((a**t-1)/(a-1))*z),'g',t,z-(Decimal(1-a))*(Decimal(s*(a**t))-Decimal((a**t-1)/(a-1))*z),'r--' )
plt.grid(True)
plt.title(r'Выплаты в остаток и в сумму')


plt.show()