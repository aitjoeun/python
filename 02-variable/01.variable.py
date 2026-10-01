# 변수 : 어떤 자료형이든 상관없이 넣을 수 있다
var1 = 'Hello Python'
print(var1)
print(id(var1))  # 주소 출력해주는 함수

var1 = 100
print(var1)
print(id(var1))

# 변수명 지정
# 변수가 무엇을 가리키는지 알 수 있는 이름으로 작명
# 예약어는 변수명으로 쓸 수 없다

# python의 자료의 크기는 상관없다
num1 = 100
num2 = 27893746238942938472734637461873468372468213746283746827346
num3 = 3.2837348399328

c = '홍길동 아무개'
s = 'Hello world!!!'
b = True

print(num1)
print(num2)
print(num3)
print(c)
print(s)
print(b)
print('-' * 30)

print('num1 type = ', type(num1))
print(f'num2 type = {type(num2)}')
print(f'num3 type = {type(num3)}')
print(f'c type = {type(c)}')
print(f's type = {type(s)}')
print(f'b type = {type(b)}')
print('-' * 30)

a = 1
b = 2
c = 3

d, e, f = 1, 2, 3
print(d, e, f)

g, h, i = '더조은', False, 3.5485
print(g, h, i)