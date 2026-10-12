# 삼항 연산식
'''
if num1 == 2:
    print('2입니다')
else :
    print('2가 아닙니다')
'''

num1 = 2
print('2입니다') if num1 == 2 else print('2가 아닙니다')
print('2입니다' if num1 == 2 else '2가 아닙니다')

# 합격, 불합격
score = 87

# 일반 조건문
if score >= 60:
    result = '합격'
else :
    result = '불합격'

# 삼항연사자로
print('합격' if score >= 60 else '불합격')

# 삼항연산자로 변수에 저장
result = '합격' if score >= 60 else '불합격'
print(result)

# 2수 중 큰수 찾기
num2 = 13
num3 = 56

max_num = num2 if num2 > num3 else num3
print(f'{num2}과 {num3}중 큰 숫자는 {max_num} 입니다')

# 회문 : 왼쪽에서 읽은것과 오른쪽으로 읽었을 때 같은 문자열