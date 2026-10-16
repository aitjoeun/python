'''
문1 : 삼각형의 넓이 구하는 파일(class) 생성
    실행하는 파일을 만들어 import하여 실행한 결과 출력

문2 : 별도의 클래스에 메소드 2개 만들기
        메소드 1 : 이름, 파이썬 점수, Ai점수를 사용자로부터 입력받기
        메소드 2 : 출력문
            출력문 ex)
            이름 : 김수영
            파이썬 : 98
            AI : 79
            합계 : 177
            평균 : 87.7
    실행파일 : 2명으로 부터 입력받아
                2명 출력하기 
'''
# 문 1
from triscore import Triangle as t
b = int(input('밑변 : '))
h = int(input('높이 : '))

area = t()
print(area.getArea(b, h))

# 문2
from triscore import Score as sc
sc1 = sc()
sc2 = sc()

sc1.set()
sc2.set()

print('='*30)
sc1.output()
print()
sc2.output()