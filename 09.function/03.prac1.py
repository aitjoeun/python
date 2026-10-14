'''
문1 : 2개의 수를 넣으면 그 사이의 숫자들의 합계 구하기
        3, 10을 매개변수로 넣으면 3~10까지의 합계를 출력

문2 : 숫자만큼 별찍기 매개변수에 3을 넣으면
*
**
***
이렇게 출력 되게

  *
 ***
*****   
'''

# 문1
def total(start, end):
    sum = 0
    for x in range(start, end+1):
        sum += x
    return sum
print(total(1, 10))
print(total(25, 78))

# 문2
def star(n):
    for x in range(n):
        for y in range(x+1):
            print('*', end='')
        print()

star(5)

def star2(n):
    for i in range(n):
        print('*' * (i+1))

star(5)


# 1행 (i=0) : 공백 4개, 별1개
# 2행 (i=1) : 공백 3개, 별3개
# 3행 (i=2) : 공백 2개, 별5개
# 4행 (i=3) : 공백 1개, 별7개
# 5행 (i=4) : 공백 0개, 별9개

def star_pyramid(rows):
    for i in range(rows):
        # space = ' ' * (rows-1-i)
        # stars = '*' * (i*2+1)
        # print(space + stars)

        print(' ' * (rows-1-i) + '*' * (i*2+1))

star_pyramid(10)