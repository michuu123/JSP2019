class lista:
    def __init__(self,l):
        self.l=l
    def sub_lists(self): 
        podLista = [[]]  
        for i in range(len(self.l) + 1):  
            for j in range(i + 1, len(self.l) + 1): 
                pod = self.l[i:j] 
                podLista.append(pod) 
        return podLista 
  

l1 = [1, 2, 3, 4] 
listeczka=lista(l1)
print(listeczka.sub_lists())
