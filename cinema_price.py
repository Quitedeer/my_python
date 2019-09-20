a=(input("Выберите фильм: "))
b=(input("Выберите дату: "))
c=int(input("Выберите время: "))
d=int(input("Укажите количество человек: "))
discont=1
if b=='tomorrow':
    discont=0.95
if d>=20:
    discont=0.8
if b=='tomorrow' and d>=20:
    discont=0.76
if a=='friday':
    if c==12:
        print(250*d*discont)
    elif c==16:
        print(350*d*discont)
    elif c==20:
        print(450*d*discont)
    else:
        print("Ошибка ввода данных")
elif a=='champions':
    if c==10:
        print(250*d*discont)
    elif c==13:
        print(350*d*discont)
    elif c==16:
        print(350*d*discont)
    else:
        print("Ошибка ввода данных")
elif a=='featherband':
    if c==10:
        print(350*d*discont)
    elif c==14:
        print(450*d*discont)
    elif c==18:
        print(450*d*discont)
    else:
        print("Ошибка ввода данных")
else:
    print("Ошибка ввода данных")
