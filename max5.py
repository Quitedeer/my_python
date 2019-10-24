L=[1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5]
M=[1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4]
def fff(x):
    s=0
    maxim=0
    ind=0
    for i in range(0,5):
        maxim+=x[i]
    for i in range(0,16):
        for i in range(i,i+5):
            s+=x[i]
        if s>maxim:
            maxim=s
            ind=i-4
        s=0
    return(x[ind:ind+5])
print(fff(L))
print(fff(M))
