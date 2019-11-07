import math
def rd(a,b):
    if(int(b)==1):
        return (a*180/math.pi)
    else:
        return ((a/180)*math.pi)
print("co chcesz przekonwertować")
print("1-radiany na stopnie")
print("2-stopnie na radiany")
x=int(input())
print("podaj wartość w wybranej uprzednio jednostce")
y=float(input())
print(rd(y,x))
