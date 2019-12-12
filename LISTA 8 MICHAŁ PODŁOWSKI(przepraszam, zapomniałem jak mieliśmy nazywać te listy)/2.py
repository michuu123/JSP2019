import os
import datetime
def cezar(tekst,klucz):
    wyraz=''
    y=''
    for x in range(len(tekst)):
        if ((ord(tekst[x])>=65)&(ord(tekst[x])<=90))|((ord(tekst[x])>=97)&(ord(tekst[x])<=122)):
            if (ord(tekst[x])>=65)&(ord(tekst[x])<=90):
                y=chr(((ord(tekst[x])-klucz-65)%26)+65)
                wyraz+=y
            if (ord(tekst[x])>=97)&(ord(tekst[x])<=122):
                y=chr(((ord(tekst[x])-klucz-97)%26)+97)
                wyraz+=y
        else:
            wyraz+=tekst[x]
    return wyraz
print("Podaj ścieżkę dostępu do folderu")
a=input()
b=a.split("\\")
c=''
pl=0
l=''
for x in range(len(b)):
    
    c+=b[x]
    if(x<len(b)-1):
        c+='\\'
print(c)
pl=0
for x in range(len(b)-1):
    l+=b[x]
    l+='\\'
    if b[x+1]in os.listdir(l):
        pl+=1
    else:
        print("Błąd, procesor ulegnie spaleniu za t = -10s")
        exit()
if pl==len(b)-1:
    print(c)
    lp=os.listdir(c)
    os.chdir(c)
    for x in lp:
        klucz1=x.split('_')
        klucz=klucz1[1]
        klucz=klucz.replace("zaszyfrowany", "")
        print(klucz)
        tekst=open(x,"r")
        deSzyfr=cezar(str(tekst.read()),int(klucz))
        data1=str(datetime.datetime.now())
        data=data1.split(' ')
        nazwa='plik_deszyfrowany'+str(klucz)+'_'+data[0]+'.txt'
        print(nazwa)
        xd = open(nazwa, 'a')
        xd.write(x+':'+chr(10)+chr(10)+deSzyfr)
        xd.close()