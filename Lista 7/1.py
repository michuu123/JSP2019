import time
def fibbo (n,a=0,b=1):
    if(n>0):
        print(a)
        b+=a
        n-=1
        fibbo(n,b,a)
    else:
        end=time.time()
        print(end-start)
a=int(input())
tr=0
start=time.time()
fibbo(a)
start=time.time()
b=int(0)
c=int(1)
for x in range(a):
    c1=c
    c+=b
    b=c1
    print(b)
end=time.time()
print(end-start)