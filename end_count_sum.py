x=1
summa=0
while x>0:
    chislo=input('Введите число: ')
    if chislo=='stop':
        print(summa)
        break
    if chislo.isdigit():
        summa=summa+float(chislo)
    else:
        print('Ошибка ввода, введите число еще раз')
