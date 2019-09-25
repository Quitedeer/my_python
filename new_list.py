N=[2,4,9,16,25]
for i in range(len(N)):
    N[i]=N[i]*N[i]
print(N)

L=[2,4,9,16,25]
L=[i*i for i in L]
print(L)

M=[2,4,9,16,25]
M=list(map((lambda i: i*i),M))
print(M)
