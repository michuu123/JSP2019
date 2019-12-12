import os
import datetime
def cezar(tekst,klucz):
    wyraz=''
    y=''
    for x in range(len(tekst)):
        if ((ord(tekst[x])>=65)&(ord(tekst[x])<=90))|((ord(tekst[x])>=97)&(ord(tekst[x])<=122)):
            if (ord(tekst[x])>=65)&(ord(tekst[x])<=90):
                y=chr(((ord(tekst[x])+klucz-65)%26)+65)
                wyraz+=y
            if (ord(tekst[x])>=97)&(ord(tekst[x])<=122):
                y=chr(((ord(tekst[x])+klucz-97)%26)+97)
                wyraz+=y
        else:
            wyraz+=tekst[x]
    return wyraz
print("Podaj ścieżkę dostępu do pliku")
a=input()
b=a.split("\\")
c=''
pl=0
l=''
for x in range(len(b)-1):
    
    c+=b[x]
    if(x<len(b)-2):
        c+='\\'
pl=0
for x in range(len(b)-1):
    l+=b[x]
    l+='\\'
    if b[x+1]in os.listdir(l):
        pl+=1
    else:
        break
if pl==len(b)-1:
    for x in os.listdir(c):
        if x==b[-1]:
            print("Plik zlokalizowany")
            os.chdir(c)
            f = open(b[-1], "r")
            pl+=1
            print("Podaj klucz szyfrowania")
            klucz=int(input())
            pSz=(cezar(f.read(),klucz))

    if(pl==0):
        print("Błąd, procesor ulegnie spaleniu za t = -10s")
        exit()
else:
    print("Błąd, procesor ulegnie spaleniu za t = -10s")
    exit()
print(pSz)

print("Szyfrowanie zakończone podaj ścieżkę końcową zakodowanego pliku")
a=input()
b=a.split("\\")
c=''
pl=0
l=''
for x in range(len(b)-1):
    
    c+=b[x]
    if(x<len(b)-2):
        c+='\\'
print(c)
for x in range(len(b)-1):
    l+=b[x]
    l+='\\'
    if b[x+1]in os.listdir(l):
        os.chdir(l)
    else:
        os.chdir(l)
        os.mkdir(b[x+1])
    print(l)
os.chdir(c+'\\'+b[-1])
data1=str(datetime.datetime.now())
data=data1.split(' ')
nazwa='plik_zaszyfrowany'+str(klucz)+'_'+data[0]+'.txt'
print(nazwa)
xd = open(nazwa, 'w')
xd.write(pSz)
xd.close()
