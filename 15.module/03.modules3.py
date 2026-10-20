import my_module3 as m

m.count = 5
print(m.count)

print(m.add(3,7))

# 클래스
student = m.Student('김마리', 25)
student.intorduce()
m.Student.hello()

# 람다 함수
print(m.square(5))