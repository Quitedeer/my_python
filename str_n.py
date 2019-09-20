s=input("Введите строчку: ")
n=input("Введите число: ")
def sravnenie(s,n):
    if len(s)>int(n):
        return(s.upper())
    else:
        return(s)
if n:
    n1=int(n)
    print(sravnenie(s,n))
else:
    print("Ошибка ввода данных")
