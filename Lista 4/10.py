print("podaj pierwszą liczbę")
a=int(input())
print("podaj drugą liczbę")
b=int(input())
f=0
if(a>b):
    for x in range(1, b+1):
        if((a%x==0)&(b%x==0)):
            f=x
else:
    for x in range(1, a+1):
        if((a%x==0)&(b%x==0)):
            f=x
print("największy wspólny dzielnik to ",f)
