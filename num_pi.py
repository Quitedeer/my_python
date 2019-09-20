x=input("Сколько знаков после запятой?")
def py_pr(x):
    from math import pi
    return f'{pi:.{x}f}'


if x:
    a=int(x)
    print(py_pr(a))
else:
    print("Вы не ввели данные")
