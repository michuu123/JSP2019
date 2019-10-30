print("podaj liczbę całkowitą")
x = int(input())

if(x%2==0):
	print("parzysta")
else:
	print("nieparzysta")

print("sposób 2")
print("podaj liczbę całkowitą")
lst = ["parzysta", "nieparzysta"]
x = int(input())
y=x%2
print(lst[y])
