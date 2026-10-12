# 무한반복으로 구구단 중 출력할 단수를 입력받아 출력
# 출력 후 구구단을 계속할 것인지 확인 'y'

while True:
    dan = int(input('몇단을 출력할지 입력 : '))
    for x in range(1, 10):
        print(f'{dan}*{x}={dan*x}')

    choose = input("계속하려면 'y'입력 : ")
    if choose == 'y' or choose == 'Y':
    # if choose.lower() == 'y':
        continue
    else:
        print('프로그램 종료')
        break 