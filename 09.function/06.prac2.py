'''
문 1 : 매개변수로 2개의 숫자와 연산자를 입력받아 출력
문 2 : 국어, 영어 점수를 사용자로 부터 입력받아
        함수로 평균을 입력받아 평균의 학점을 return 하기
문 3: 로또를 함수로
문 4 :
입력한 비밀번호가 비밀번호 규칙에 맞으면 생성되고,
규칙에 맞지 않으면 다시 생성하도록 메시지를 출력하는 프로그램을 작성
1. 8글자 이상이어야 함
2. 문자 및 숫자로만 생성해야 하며 기호는 불가능

새로운 비밀번호를 입력하세요 : abcd
오류. 비밀번호가 규칙에 맞지 않습니다

새로운 비밀번호를 입력하세요 : abcd1234$$$
오류. 비밀번호가 규칙에 맞지 않습니다

새로운 비밀번호를 입력하세요 : 1234abcd
비밀번호가 생성 되었습니다
'''
import random
# 문1
def calc(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2
    return result

# val1 = int(input('숫자입력 : '))
# val2 = int(input('숫자입력 : '))
# oper = input('연산입력 : ')
# print(calc(val1, val2, oper))

# 문제 2
# kor = int(input('국어점수 입력 : '))
# eng = int(input('영어점수 입력 : '))
# avg = (kor+eng) / 2

# def grade(avg):
#     if avg >= 90: return 'A'
#     elif avg >= 80: return 'B'
#     elif avg >= 70: return 'C'
#     elif avg >= 60: return 'D'
#     else: return 'F'

# print(grade(avg), '학점')

# 문 3
def lotto():
    lotto_set = set()
    while len(lotto_set) < 6:
        num = random.randint(1,45)
        lotto_set.add(num)

    lotto_list = sorted(lotto_set)
    print(f'오늘의 행운번호 :', lotto_list)

lotto()

# 문4
def checkPwd(pwd):
    # if len(pwd) < 8 :
    #     return False
    # if pwd.isalnum() :
    #     return True
    # else:
    #     return False
    if len(pwd) >= 8 and pwd.isalnum():
        return True
    else:
        return False

password = input('비밀번호 입력 : ')
if checkPwd(password):
    print('비밀번호가 생성되었습니다')
else:
    print('비밀번호 규칙에 맞지 않습니다')