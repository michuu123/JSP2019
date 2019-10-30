import os
print("podaj liczbę kolumn")
n=int(input())
print("podaj liczbę wierszy")
m=int(input())
for x in range(1, m+1):
	z=''
	for y in range(1, n+1):
		z+="\t"
		z+=str(x*y)
	print(z)
		
os.system("PAUSE")
