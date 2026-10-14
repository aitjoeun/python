'''
문 : 사용자로부터 전화번호 입력 받아(010-2345-3456)
    하이픈을 제거하고
    오직 숫자로만 구성되어 있는지 확인하기
    숫자중 '0'의 갯수 세기
'''
phone = input('전화번호 입력 "-"포함 : ')
print(phone)

# 하이픈 제거
number = phone.replace('-','')
print(number)

isNum = number.isdigit()
print(isNum)

if isNum:
    zero_count = number.count('0')
    print('0의 갯수 : ', zero_count)
else:
    print('잘못입력 하였습니다')