age = int(input('나이 입력 : '))
# 방법 1
if age > 19:
    print('성년 입니다')
elif age >= 15 :
    print('청소년 입니다')
else:
    print('어린이 입니다')

# 방법2
if age <= 19:
    if age >= 15:
        print('청소년 입니다')
    else :
        print('어린이 입니다')
else:
    print('성년 입니다')

