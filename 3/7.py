import os
print("jak długi ma być ciąg fibonachiego")
x=int(input())
y=range(1,x)
f1=0
f2=1

for z in y:
	print(f1)
	f2+=f1
	print(f2)
	f1+=f2
	
	
os.system("PAUSE")
