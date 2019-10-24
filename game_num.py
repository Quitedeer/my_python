import random
a=3
b=random.randint(0,10)
print('Lets play')
while a>0:
    print('You have',a,' tries. Good luck!')
    x=input('It is:')
    if x=='stop':
        break
    elif b==int(x):
        print('Victory')
        break
    elif b<int(x):
        print('It is smaller')
        a=a-1
    else:
        print('It is bigger')
        a=a-1
    if a==0:
        print('Game over', b)
