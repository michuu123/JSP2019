a=str(1)
n=int(input())
for x in range(n):
    if n>0:
        if(n>0):
            f=a[0]
            g=0
            h=''
            for y in a+' ':
                if(f==y):
                    g+=1
                else:
                    h+=str(g)
                    h+=f
                    f=y
                    g=1
            a=h
            print(h)
            n-=1
        else:
            break