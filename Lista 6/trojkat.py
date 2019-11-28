import math
def obwod(a,b,c):
    return a+b+c
def pole(a,b,c):
    return math.sqrt(((a+b+c)*(a+b)*(a+c)*(b+c))/16)
def kat(a,b,c):
    e=[]
    e.append(int(a))
    e.append(int(b))
    e.append(int(c))
    e.sort()
    return math.acos(((e[-1]**2)-(e[0]**2)-(e[1]**2))/(-2*e[0]*e[1]))
def kat1(a,b,c):
    if((math.degrees(kat(a,b,c)))==float(90)):
        return "Trójkąt jest prostokątkny"
    else:
        if((math.degrees(kat(a,b,c)))>float(90)):
            return "Trójkąt jest rozwartokątkny"
        else:
            return "Trójkąt jest ostrokątny"
def boki(a,b,c):
    e=[]
    e.append(a)
    e.append(b)
    e.append(c)
    y=int(0)
    for x in e:
        if (e.count(int(x)))>y:
            y=(e.count(int(x)))
    if y==3:
        return "równoboczny"
    if y==2:
        return "równoramienny"
    if y==1:
        return "różnoboczny"