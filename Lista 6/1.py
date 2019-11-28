import trojkat
import math
print("Podaj bok a")
a=int(input())
print("Podaj bok b")
b=int(input())
print("Podaj bok c")
c=int(input())
e=[]
e.append(a)
e.append(b)
e.append(c)
e.sort()
if (e[0]+e[1])>e[2]:
    print("Obwód: "+str(trojkat.obwod(a,b,c)))
    print("Pole "+str(trojkat.pole(a,b,c)))
    print("Kąt "+str(math.degrees(trojkat.kat(a,b,c))))
    print(trojkat.kat1(a,b,c))
    print(trojkat.boki(a,b,c))
else:
    print("to nie jest trójkąt >:(")