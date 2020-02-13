change = input('영어 입력:')
print('대문자\n', change.upper())
print('소문자\n', change.lower())

new_change = str()

for w in change :
    if w.islower() :
        new_change += w.upper()
    else :
        new_change += w.lower()

print('대소문자 체인지\n', new_change)

print('대소문자 체인지\n', change.swapcase())



e = input('영어 입력 :')

e_n = str()

for n in range(len(e)-1, -1, -1):
    e_n += e[n]

print(e_n)

print(e[::-1])
