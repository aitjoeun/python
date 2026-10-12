# 사용자로부터 2수 입력을 받고, 연산자도 입력받음
# 연산 결과를 출력하기
#  +, -, *, /, //, %, **
num1 = int(input('첫번째 숫자 입력 : '))
num2 = int(input('두번째 숫자 입력 : '))
op = input('연산자 입력 : ')

result = 0

if op == '+':
    result = num1 + num2
if op == '-':
    result = num1 - num2
if op == '*':
    result = num1 * num2
if op == '/':
    result = num1 / num2
if op == '//':
    result = num1 // num2
if op == '%':
    result = num1 % num2
if op == '**':
    result = num1 ** num2
    # print(num1, op, num2, '=', num1**num2)

print(num1, op, num2, '=', result)

# 숫자를 입력받아
# 양수, 홀수(짝수) 인지
# 음수, 홀수(짝수) 인지

if num1 > 0:
    print('양수 입니다')
    if num1 % 2 == 0:
        print('짝수 입니다')
    else:
        print('홀수 입니다')
elif num1 < 0:
    print('음수 입니다')
    if num1 % 2 == 0:
        print('짝수 입니다')
    else:
        print('홀수 입니다')
else :
    print('0입니다')

if num1 == 0:
    print('0입니다')
else:
    if num1 > 0:
        print('양수입니다')
    else :
        print('음수 입니다')

    if num1 % 2 == 0:
        print('짝수입니다')
    else :
        print('홀수 입니다')
print('-' * 30)

if num1 == 0:
    print('0입니다')
else:
    sign = '양수' if num1 > 0 else '음수'
    parity = '짝수' if num1 % 2 == 0 else '홀수'

    print(sign, '입니다')
    print(parity, '입니다')
