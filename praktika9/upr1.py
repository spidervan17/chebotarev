eps1=1
eps2=eps1*0.5
eps3=eps2+1
while eps3>1:
    eps1=eps2
    eps2=eps1*0.5
    eps3=eps2+1
print(eps1)