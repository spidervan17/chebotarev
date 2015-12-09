s = open('input.txt')
s=s.read()
s=s.lower()
s=s.replace('!', ' ').replace('?', ' ').replace('.', ' ').replace(',', ' ')
Slova=[]
for elem in s.split():
    Slova.append(elem)
Sh={}
for shtuka in Slova:
    Sh[(shtuka)]=Slova.count(shtuka)
print(Sh)
print(max(Sh))