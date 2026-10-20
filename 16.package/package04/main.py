import student

name = '김수완'
# *args일 때
# avg = student.average(90, 89, 29, 98)

# **kwargs일 때
avg = student.average(kor=90, eng=89, math=29, com=98)

grade = student.get_grade(avg)

# print('이름 :', name)
# print('평균점수 :', avg)
# print('학점 :', grade)
student.print_info(name, avg, grade)