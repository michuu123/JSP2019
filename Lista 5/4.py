def koduj(c):
    code = {"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e"}
    decode = {"y":"a","i":"e","o":"i","a":"o","e":"y"}
    d=''
    for x in range(0,len(c)):
        if(((c[x])=='a')|((c[x])=='e')|((c[x])=='i')|((c[x])=='o')|((c[x])=='y')):
            d+=code[c[x]]
        else:
            d+=c[x]
    return d
def dekoduj(c):
    code = {"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e"}
    decode = {"y":"a","i":"e","o":"i","a":"o","e":"y"}
    d=''
    for x in range(0,len(c)):
        if(((c[x])=='a')|((c[x])=='e')|((c[x])=='i')|((c[x])=='o')|((c[x])=='y')):
            d+=decode[c[x]]
        else:
            d+=c[x]
    return d
c=input()
print(koduj(c))
print(dekoduj(koduj(c)))
