s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
for i in range(len(s)):
    if s[i]=='м':
        if s[i-1]!=' ':
            continue
    else:
        L=''.join(s)
print(L)
