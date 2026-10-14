# Comprehension
# for문이나 if문을 한줄에 넣는다
#    특히 리스트에서 많이 사용 -> list comprehension 불림

result = [0 for i in range(100)]
print(result)

result = [10 for x in range(100)]
print(result)

result = [i+1 for i in range(100)]
print(result)

result = ['더조은' for i in range(100)]
print(result)

data = [3, 5, 7, 9]
result = [x**2 for x in data]
print(result)

# numList = [int(input('숫자입력 : ')) for x in range(5)]
# print(numList)
# print('합계 : ', sum(numList))

# if와 for문이 함께 들어 있을 때 무조건 for문부터
#   if만 있는 경우는 맨 뒤에
#   if-else 있는 경우는 맨 앞에

print('-' * 30)
result = []
for num in range(1, 20):
    if num % 2 == 0:
        result.append(num*3)

result = [num*3 for num in range(1,20) if num % 2 == 0]
print(result)

result = []
for num in range(1,10):
    if num % 2 == 0:
        result.append(num)
    else:
        result.append(0)

result = [num if num % 2 == 0 else 0 for num in range(1,10)]
print(result)

# 1~5까지
# ['홀수','짝수','홀수','짝수','홀수']
result = ['짝수' if num % 2 == 0 else '홀수' for num in range(1,10)]
print(result)

# for문이 중첩으로 들어갈때
result = []