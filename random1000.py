import random
L=[random.randint(-100,100) for i in range(1,1000)]
def fff(x):
    kol=0
    if L.index(min(L))>L.index(max(L)):
        for i in range(L.index(max(L)),L.index(min(L))):
            if L[i]<0:
                kol+=1
    else:
        for i in range(L.index(min(L)),L.index(max(L))):
            if L[i]<0:
                kol+=1
    if min(L)<0:
        kol+=1
    if max(L)>0:
        kol+=1
    return(kol)
print(fff(L))
