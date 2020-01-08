class Koło:
    def __init__(self,r):
        self.r=r
    def pole(self):
        return (self.r**2)*3.14
    def obwod(self):
        return self.r*2*3.14
a=int(input())
kolo=Koło(a)

print(kolo.pole())
print(kolo.obwod())
