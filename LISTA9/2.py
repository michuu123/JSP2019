import numpy as np
print("w jaki sposób chcesz podać dane")
print("0-ręcznie")
print("1-z pliku")
a=input()
d=[]
if(a=='0'):
    print("ile danych zamierzysz wprowadzić")
    b=int(input())
    if b==0:
        print("w takim razie nie zawracaj mi głowy >:(")
    else:
        for x in range(b):
            c=int(input())
            d.append(c)
        d1=np.asarray(d)
        print(d1)
        print(np.mean(d1))
        print(np.var(d1))
        print(np.std(d1))

            


else:
    print("Podaj lokalizację pliku")
    plik=input()
    f = open(plik,'r')
    d=f.read().split(" ")
    for x in range(len(d)):
        d[x]=int(d[x])
    d1=np.asarray(d)
    print(d1)
    print(np.mean(d1))
    print(np.var(d1))
    print(np.std(d1))