s = open('en-ru.txt')
text=open('input.txt')
text=text.read()
text=text.rstrip()
s=s.read()
s=s.lower()
s=s.replace('-', ' ')
Slova=[]
output = open('output1.txt', 'w')

for elem in s.split():
    Slova.append(elem)
Sh={}
for shtuka in range(len(Slova)-1):
    if shtuka%2==0:
        Sh[(Slova[shtuka])]=Slova[shtuka+1]
text=text.lower()
text1=text[(text.find('.')+1):]
text2=text[0:text.find('.')]
while text1!='':
    a=''
    W=''
    text2=text2.replace('.', ' ')
    for elem in text2.split():
        a=elem
        if a in Sh:
            a=Sh[a]
        W=W+a+' '
    u=W.rfind(' ')
    W=W[0:u-1]+'.'
    print(W, file=output)
    text2=text1[:(text.find('.'))]
    text1=text1[(text.find('.')+1):]