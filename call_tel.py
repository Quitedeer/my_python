x=input("Введите время звонка в минутах:")
y=input("Введите код города: ")
if x:
    vrem=float(x)
    if y:
        kod_gor=int(y)
        if kod_gor==343: print("Стоимость звонка в городе Екатеринбург:", 15*vrem)
        elif kod_gor==381: print("Стоимость звонка в городе Омск:", 18*vrem)
        elif kod_gor==473: print("Стоимость звонка в городе Воронеж:", 13*vrem)
        elif kod_gor==485: print("Стоимость звонка в городе Ярославль:", 11*vrem)
        else: print("Город неопределен")
    else:
        print("Вы не ввели код города!!!")
else:
    print("Вы не ввели время звонка!!!")
