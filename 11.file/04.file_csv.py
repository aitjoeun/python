'''
students = []
with open('11.file/test.csv', 'r') as f:
    lines = f.readlines()
    print(lines)

    for line in lines:
        # line = line.strip()
        # print(line)
        # line = line.split(',')
        # print(line)
        # students.append(line)

        # 3줄을 한줄로
        students.append(line.strip().split(','))

print(students)


students2 = []
with open('11.file/test.csv', 'r') as f:
    lines = f.read().splitlines()
    print(lines)

    for line in lines:
        # line = line.split(',')
        # print(line)
        # students2.append(line)

        # 위의 2줄을 한줄로
        students2.append(line.split(','))
    
print(students2)
'''

with open('11.file/test.csv', 'r') as f:
    students3 = [line.split(',')  for line in f.read().splitlines()]
print(students3)

# 이름 : 더조은, 국어:90, 영어:80, 수학:80, 컴퓨터:78, 총점: 358, 평균 : 87.2

result = ''
for student in students3:
    name, kor, eng, math = student
    total = int(kor) + int(eng) + int(math)
    avg = total/3

    result += f'이름:{name}, 국어:{kor}, 영어:{eng}, 수학:{math}, 총점:{total}, 평균:{avg:.1f}\n'

print(result)

with open('11.file/result.txt', 'w') as f:
    f.write(result)