st1 = '       He likes apples, and she does, too     '

# 좌우 공백 제거
st2 = st1.strip()
print(st1 + '=====')
print(st2 + '=====')
print('-' * 60)

# 오른쪽 공백 제거
st2 =st1.rstrip()
print(st1 + '=====')
print(st2 + '=====')
print('-' * 60)

# 왼쪽 공백제거
st2 = st1.lstrip()
print(st1 + '=====')
print(st2 + '=====')
print('-' * 60)

# 문자열 바꾸기
st2 = st1.replace('like', 'love')
print(st1)
print(st2)

st2 = st1.replace('like', 'love', 1)
print(st1)
print(st2)

st2 = st1.replace(' ', '')
print(st1)
print(st2)