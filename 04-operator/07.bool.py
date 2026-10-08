'''
bool() 변환

False가 되는 경우
    : 완전히 비어 있거나 0인 경우(0, 0.0, ''(빈문자열), None, [](빈리스트)등)
True가 되는 경우
    : 그 외에 데이터가 하나라도 들어있는 경우(5, 5.8, ' '(공백 한글자))    
'''

print(bool(5))
print(bool(0))
print('-' * 20)

print(bool('박인나'))
print(bool(''))
print(bool(' '))
print('-' * 20)

print(bool(5.7))
print(bool(0.0))
print('-' * 20)

a = 5
b = None
print(bool(a))
print(bool(b))

name = input('이름 입력 : ')
print(bool(name))
print('name =', name)