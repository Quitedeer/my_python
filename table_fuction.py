x=input("Введите номер элемента: ")
if x:
    num_el=float(x)
    if num_el==3:
        print("Ваш элемент - литий")
    elif num_el==17:
        print("Ваш элемент - хлор")
    elif num_el==25:
        print("Ваш элемент - марганец")
    elif num_el==80:
        print("Ваш элемент - ртуть")
    else:
        print("Что это??")
else:
    print("Введите номер элемента!!!")
