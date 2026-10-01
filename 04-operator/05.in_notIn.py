'''
소속연산자
in : 어떤 데이터가 특정 데이터안에 있는지 검사
    -> True : 있다
    -> False : 없다

not in : 어떤 데이터가 특정 데이터안에 없는지 검사
    -> True : 없다
    -> False : 있다
'''
str = 'abcdefg'
print('bc' in str)
print('df' in str)
print('xy' in str)
print('-' * 20)

print('bc' not in str)
print('df' not in str)
print('xy' not in str)