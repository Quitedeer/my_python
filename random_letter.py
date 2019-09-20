L=['python','computer','game']
import random
a=random.randint(0,2)
b=len(L[a])
c=random.randint(0,b-1)
lst=list(str(L[a]))
d=lst[c]
lst[c]='?'
print(''.join(lst))
x=input("Какой буквы нет?")
if x==d:
    print("Победа!!!")
else:
    print("Увы, попробуйте снова")
