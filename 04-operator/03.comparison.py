# 비교 연산자 : 비교결과가 True, False로 출력
# >, <, >=, <=
# ==, !=

num1 = int(input('첫번째 정수 입력 : '))
num2 = int(input('두번째 정수 입력 : '))

print(f'첫번째 숫자가 두번째 숫자보다 큰가? {num1 > num2}')
print(f'첫번째 숫자가 두번째 숫자보다 큰거나 같은가? {num1 >= num2}')
print(f'첫번째 숫자가 두번째 숫자보다 작은가? {num1 < num2}')
print(f'첫번째 숫자가 두번째 숫자보다 작거나 같은가? {num1 <= num2}')
print(f'첫번째 숫자와 두번째 숫자가 같은가? {num1 == num2}')
print(f'첫번째 숫자와 두번째 숫자가 다른가? {num1 != num2}')