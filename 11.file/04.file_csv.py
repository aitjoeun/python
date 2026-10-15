students = []
with open('11.file/test.csv', 'r') as f:
    lines = f.readlines()
    print(lines)

    for line in lines:
        line = line.strip()
        print(line)
        line = line.split(',')
        print(line)
        students.append(line)

print(students)


students2 = []
with open('11.file/test.csv', 'r') as f:
    lines = f.read().splitlines()
    print(lines)

    for line in lines:
        line = line.split(',')
        print(line)
        students2.append(line)

print(students2)

