import math
x = int(input('Введите число: '))
a=0
while x>0:
    if x%2==1:
        a=a+math.pow(x%10,2)
    else:
        a=a
    x=x//10
if a==0:
    print('Все цифры числа - четные')
else:
    print(a)
