f=[6,3,5,2]
print("""
1-suma
2-iloczyn""")
a=int(input())
if a==2:
    z=int(1)
    for x in f:
        z*=x
    print(z)
if a==1:
    z=int(0)
    for x in f:
        z+=x
    print(z)
