#--------구구단출력
for n in range(1,10):
    print (1, 'x', n,'=', 1*n)

for n in range(1,10):
    print (2, 'x', n, '=', 2*n)
    
#--------모든 구구단
for n in range(1,10):
    print ('='*10)
    for m in range(1,10):
        print (n, 'x', m, '=', n*m)


#---------구구단입력
number = int(input ('구구단을 몇 단 출력할까요? 숫자를 입력하세요:'))
while number > 9 or number < 1 :
    number = int(input ('다시 숫자를 입력하세요:'))
    
for n in range(1,10) :
    print (number, 'x', n, '=', number*n)

