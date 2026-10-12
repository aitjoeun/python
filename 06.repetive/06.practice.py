# 문 : 2개의 숫자를 입력받아 합계 구하기. 무한반복
#      사용자가 첫번째 값에 0을 넣으면 종료

while True:
    num1 = int(input('숫자 1(종료하려면 0) : '))
    if num1 == 0:
        break
    num2 = int(input('숫자 2 : '))

    print(f'{num1} + {num2} = {num1+num2}\n')
print('계산 종료')