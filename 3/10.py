import os
f=[]
for x in range (100, 401):
	y=x
	z=int(0)
	while y>0:
		if(int(y)%10)%2==0:

			z+=1
			y=int(y/10)
		else:
			
			break
		if(z==3):
		    f.append(str(x))
		
print(','.join(f))
os.system("PAUSE")

