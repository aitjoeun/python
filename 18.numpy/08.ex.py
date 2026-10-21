import numpy as np

# 1. 1차원 배열 생성
# [10 20 30 40 50]
a1 = np.array([10, 20, 30, 40, 50])
print(a1)
print()

a1 = np.arange(10, 60, 10)
print(a1)
print('-'*30)

# 2. 2차원 배열 생성
# [[1 2 3]
#  [4 5 6]]
a2 = np.array([[1, 2, 3],
               [4, 5, 6]])
print(a2)
print('-'*30)

# 3. 5부터 20까지(20도 포함) 3씩 증가하는 1차원 배열을 생성
a3 = np.arange(5, 21, 3)
print(a3)
print('-'*30)

# 4. 1부터 12까지의 숫자를 생성한 뒤, 3행 4열의 배열로 변환
a4 = np.arange(1, 13).reshape(3, 4)
print(a4)
print('-'*30)

# 5. 0부터 1까지 동일한 간격으로 나누어진 숫자 6개를 생성
a5 = np.linspace(0, 1, 6)
print(a5)
print('-'*30)

# 6. 모든 원소가 0인 3행 4열의 배열 생성
a6 = np.zeros((3,4))
print(a6)
print('-'*30)

# 7. 모든 원소가 1인 2행 5열의 배열 생성. 단, 데이터 타입은 정수형으로
a7 = np.ones((2,5), dtype=int)
print(a7)
print('-'*30)

# 8. 다음 조건을 만족하는 배열 생성
# - 2부터 24까지 짝수를 생성
# - 생성한 배열을 3행 4열로 변환한다.
a8 = np.arange(2, 25, 2).reshape(3, 4)
print(a8)
print('-'*30)

# 9. 다음 조건을 만족하는 배열을 생성
# - 10부터 50까지 균등한 간격의 숫자 9개를 생성
# - 생성한 배열을 3행 3열로 변환
a9 = np.linspace(10, 50, 9).reshape(3, 3)
print(a9)
print('-'*30)

# 10. 다음 세 가지 배열을 각각 생성
# 1. arange()와 reshape()를 사용해 1부터 16까지의 숫자를 4행 4열로 만든다.
# 2. 모든 원소가 0인 4행 4열의 배열을 만든다.
# 3. 모든 원소가 1인 4행 4열의 정수형 배열을 만든다.
b = np.arange(1, 17).reshape(4, 4)
c = np.zeros((4,4))
d = np.ones((4,4), dtype=int)
print(b)
print(c)
print(d)
print('-'*30)

# 11. 4행 4열의 단위행렬을 생성(자료형 정수형(int))
a11 = np.identity(4, dtype=int)
print(a11)
print('-'*30)

# 12. 3행 5열의 배열에서 주대각선보다 한 칸 오른쪽에 1이 위치하도록 만들기
#     자료형은 정수형으로 지정
a12 = np.eye(3, 5, k=1, dtype=int)
print(a12)