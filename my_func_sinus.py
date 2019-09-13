import math
value = input("Введите х:")
if value:
    x = float(value)
    if 0.2<=x<=0.9:
        print(math.sin(x))
    else: print("f=1")
else:
    print("Нужно ввести число!")
