value = input("Введите х:")
if value:
    x = float(value)
    if -2.4<=x<=5.7:
        print("f=", x*x)
    else: print("f=4")
else:
    print("Нужно ввести число!")
