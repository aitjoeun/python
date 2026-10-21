import numpy as np

arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])

# 행렬곱
print('행렬곱 :')
print(np.dot(arr1, arr2))
print(arr1 @ arr2)

# 전치행렬 : 행과 열을 바꿈
print('전치행렬 :')
print(np.transpose(arr1))
print(arr1.T)

# 행렬식 : 행렬이 공간을 얼마나 늘리거나 줄였는지(확대/축소 비율)
# det() 함수 사용 -> det(A) = -2
print('행렬식 :')
print(np.linalg.det(arr1))

# 위의 행렬식에서 0이나오면 역행렬은 존재하지 않음
# 역행렬
print('역행렬 :')
print(np.linalg.inv(arr1))

if np.linalg.det(arr1) != 0:
    inv_arr1 = np.linalg.inv(arr1)
    print(f'역행렬 : {inv_arr1}')

    print('검증 :')
    print(np.round(arr1 @ inv_arr1))
else:
    print('행렬식이 0이므로 역행렬이 존재하지 않습니다')