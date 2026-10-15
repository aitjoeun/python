# 가변 키워드 인자
# **kwargs : dictionary가 전달됨

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)

print_info(name='최명길')
print_info(name='김미영', age='23', city='Seoul')

# 딕셔너리를 넘겨줘도 됨
info = {'name' : '이사람', 'age' : 25, 'city' : 'Gyeongi-do'}
print_info(**info)
