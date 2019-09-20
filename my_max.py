x=input("Введите первое число: ")
y=input("Введите второе число: ")   
def my_max(x,y):
    if x:
        x1=float(x)
        if y:
            y1=float(y)
            if x>y:
                return x
            elif x<y:
                return y
            else:
                return("Числа равны")
        else:
            return("Вы не ввели второе число!!!")
    else:
        return("Вы не ввели первое число!!!")


print(my_max(x,y))
