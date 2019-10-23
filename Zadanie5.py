import os
import math

y=input()
b=input()
x=float(len(y))
if x/2==x//2:
	z=int(x/2)
	a=y[0:z]+b+y[z:int(x)]
	print(a)
else:
	z=int(x/2)+1
	a=y[0:z]+b+y[z:int(x)]
	print(a)
os.system("PAUSE")



