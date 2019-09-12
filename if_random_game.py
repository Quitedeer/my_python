import random
x = random.randint(1,4)
y = int(input("Ты думаешь, что я загадал число: "))
if x == y:
    print("Ты победил!!")
elif x<y:
    print("Нет, мое число меньше...")
elif x>y:
    print("Нет, мое число больше...")
