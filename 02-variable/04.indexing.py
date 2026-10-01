# indexing

str1 = 'abcdefghijk'
print(str1[0])
print(str1[2])
print('-' * 30)

# 음수는 뒤에 부터, -1부터 시작
print(str1[-1])
print(str1[-4])
print('-' * 30)

# slicing
# [시작:끝:step] => step생략가능 생략하면 default = 1
#                   끝은 포함 안함        
print(str1[1:4])
print(str1[:3])
print(str1[2:])
print(str1[:])
print('-' * 30)

print(str1[1:9:2])
print(str1[1:9:3])
print(str1[::3])
print(str1[::-3])  # 순서를 뒤집어서 가져올 때
print(str1[5:1:-1])
print(str1[-1:-6:-1])
print('-' * 30)

# 문자열 연결하기 : +
str2 = 'xyz'
str3 = str1 + str2
print(str3)

# 문자열 반복하기 : *
str4 = str2 * 3
print(str4)

# 문자열의 갯수 확인
print(len(str1))
print('-' * 30)

# 문자열은 인덱싱으로 문자열을 부분적으로 변경못함.
#  str1[0] = 'z'
str1 = 'z' + str1[1:]
print(str1)