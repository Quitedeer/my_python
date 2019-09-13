import random
x = random.randint(1,4)
y = int(input("Я загадал число от 1 до 4. Ты думаешь, что это число: "))
if x == y:
    print("Ты победил!!")
elif x<y:
    print("Нет, мое число меньше...")
else:
    print("Нет, мое число больше...")
