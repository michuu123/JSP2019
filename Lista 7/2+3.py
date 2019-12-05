import random
import time
a=int(1000)
b=[]
for x in range(a):
    b.append(random.randint(0,1000))
print(b)
c=b
y=b[0]
start=time.time()
for x in range(a):
    for y in range(a):
        if(b[y]>b[x]):
            b.insert(y,b[x])
            if(y<x):
                b.pop(x+1)
            else:
                b.pop(x)
            break
end=time.time()
"print(b)"
print(end-start)
start=time.time()
for x in range(a-1):
    if ((c[x]>c[x+1])&(a>1)):
        d=c[x+1]
        c[x+1]=c[x]
        c[x]=d
    a-=1
end=time.time()
'print(b)'
print(end-start)