s="У лукоморья 123 дуб зеленый 456"
print("Индекс буквы я в строке: ", s.index("я"))
print("Буква у встречается в строке ", s.count("у"), " раз")
if s.isalpha()==False:
    print(s.upper())
if len(s)>4:
    print(s.lower())
print(s.replace("У","О"))
