import os
def sqrt(a,b,c):
	if(a==0):
		print("to nie jest równanie kwadratowe")
	else:
		dlt=(b**2)-(4*(a*c))
		x2=(((b*(-1)) - (dlt**(1/2)))/(2*a))
		x1=(((b*(-1)) + (dlt**(1/2)))/(2*a))
	return x1, x2

print("podaj a ")
a=int(input())
print("podaj b ")
b=int(input())
print("podaj c ")
c=int(input())
print(sqrt(a,b,c))

os.system("PAUSE")
