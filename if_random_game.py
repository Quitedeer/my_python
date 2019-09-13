import random
x = random.randint(1,4)
value = input("Я загадал число от 1 до 4. Ты думаешь, что это число: ")
if value:
    y = float(value)
    if x==y:
        print("Ты победил!!")
    elif x<y:
        print("Нет, мое число меньше...Повторите ее раз!")
    else:
        print("Нет, мое число больше...Повторите ее раз!")
else:
    print("Нужно ввести число!")
