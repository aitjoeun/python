# 문1 : 정수를 입력받아 짝수인지 홀수인지 판별
num = int(input('정수 입력 : '))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')
    
# 문2 : 2개의 정수를 입력받아 큰값과 작은값을 판별하여 출력
# ex) 3,7입력 -> 큰값 : 7, 작은값 : 3
num1 = int(input('첫번째 정수 입력 : '))
num2 = int(input('두번째 정수 입력 : '))

if num1 > num2:
    print(f'큰값 : {num1}, 작은값 : {num2}')
else:
    print(f'큰값 : {num2}, 작은값 : {num1}')

if num2 > num1:
    num1, num2 = num2, num1

print(f'큰값 : {num1}, 작은값: {num2}')     