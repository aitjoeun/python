import numpy as np

# 단위행렬
# 행과 열이 같은 n x n 의 대각선이 모두 1이고 나머지는 0인 행렬
print(np.identity(5))

# 직사각 행렬
# eye(N, M=None, k=0, dtype=float)함수
# N(필수) : 행(row)의 개수
# M(선택) : 열의 개수(지정하지 않으면 정방행렬 생성)
# k(선택) : 1을 채울 대각선의 위치
# dtype(선택) : 배열의 데이터 타입