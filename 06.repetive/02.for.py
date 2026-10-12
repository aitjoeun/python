# 02.for.py

# 1~ 100합계
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 1~100까지 5의 배수의 합
sum = 0
for z in range(1, 101):
    if(z % 5 == 0):
        sum += z
print('1~100까지 5의 배수의 합 :', sum)

sum = 0
for n in range(0, 101, 5):
    sum += n
print('1~100까지 5의 배수의 합 :', sum)