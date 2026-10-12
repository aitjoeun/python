import random
# x = random.random()
# i = random.randint(1,3) # end포함  1,2,3중에서 랜덤으로
# print(x)
# print(i)

# 문 : 주사위를 3개를 동시에 던져서 동일한 숫자가 나오면 탈출하는 게임
# 출력. 주사위에 나온 숫자와 횟수 출력
count = 0
while True:
    count += 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)

    # if(dice1 == dice2) and (dice2 == dice3):
    if dice1 == dice2 == dice3:
        break
print('주사위의 숫자 :', dice1)
print(count, '번에 맞혔습니다')


# 문 : 주사위의 숫자 맞추기. 몇회만에 맞췄는지. 맞힐때까지 무한반복
count = 0
while True:
    count += 1
    com = random.randint(1,6)
    user = int(input('주사위의 숫자는 어떤 숫자일까요? '))
    if com == user:
        print('정답입니다.', count, '회에 맞췄습니다.')
        break
    else:
        print('안타깝네요', com, '입니다. 다시합니다')
        continue