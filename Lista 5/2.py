def liczbyNaSlowa(liczba):
    j={1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery",5:"pięć",6:"sześć",7:"siedem",8:"osiem",9:"dziewięć",10:"dziesięć",11:"jedenaście",12:"dwanaście",13:"trzynaście",14:"czternaście",15:"piętnaście",16:"szesnaście",17:"siedemnaście",18:"osiemnaście",19:"dziewiętnaście"}
    liczba1=int(liczba)
    slowa=['','','','']
    lop = int(3)
    while liczba>0:
        if(lop==3):
            if(liczba%10!=0):
                slowa[lop]=j[liczba%10]
        if(lop==2):
            if(liczba%10==1):
                if(liczba1%10==0):
                    slowa[lop]='dziesięć'
                    slowa[3]=''
                else:    
                    slowa[lop]=j[liczba1%100]
                    slowa[3]=''
            else:
                if(liczba%10==2):
                    slowa[lop]='dwadzieścia'
                if(liczba%10==3):
                    slowa[lop]='trzydzieści'
                if(liczba%10==4):
                    slowa[lop]='czterdzieści'
                if(liczba%10>4):
                    slowa[lop]=j[liczba%10]+'dziesiąt'
        if(lop==1):
            if(liczba%10==1):
                slowa[lop]='sto'
            if(liczba%10==2):
                slowa[lop]='dwieście'
            if(liczba%10==3):
                slowa[lop]='trzysta'
            if(liczba%10==4):
                slowa[lop]='czterysta'
            if(liczba%10>4):
                slowa[lop]=j[liczba%10]+'set'
        if(lop==0):
            if(liczba%10==1):
                slowa[lop]='tysiąc'
            if((liczba%10>1)&(liczba%10<5)):
               slowa[lop]=j[liczba%10]+' tysiące'
            if(liczba%10>4):
               slowa[lop]=j[liczba%10]+' tysięcy'
    
        
        liczba=int(liczba/10)
        lop-=1
    koniec=''
    for x in slowa:
        koniec+=x
        koniec+=' '
    
    return koniec
x=int(input())
print(liczbyNaSlowa(x))
