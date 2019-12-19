import math as m
import numpy as np
import matplotlib.pyplot as plt
g=10
n=10
print("podaj kąt rzutu w stopniach")
a=int(input())
print("podaj prędkość początkową")
v=int(input())
vy=v*m.sin(m.radians(a))
vx=v*m.cos(m.radians(a))
trz=2*vy/g
print("Czas rzutu wynosi ",trz,"s")
xk=vx*trz
print("Zasięg rzutu wynosi ",xk,"m")
print("Ciało wzniesie się na wysokość ",vy*((1/2)*trz),"m")
t=np.linspace(0,trz,n)
vx1=np.linspace(vx,vx,n)
plt.subplot(3,1,1)
plt.plot(t,vx1)
vy1=vy-(g*t)
plt.subplot(3,1,1)
plt.plot(t,vy1)
plt.ylabel('v[m/s]')
plt.xlabel('t[s]')
plt.subplot(3,1,3)
x=vx1*t
y=vy*t+vy1*t
plt.ylabel('y[m]')
plt.xlabel('x[m]')
plt.plot(x,y)
plt.subplot(3,1,2)
plt.plot((x**2+y**2)**(1/2),t)
plt.xlabel('t[s]')
plt.ylabel('r[m]')
plt.show()