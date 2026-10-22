import numpy as np

a = np.array([
    [[1,2,3],
     [4,5,6]],

    [[7,8,9],
     [10,11,12]]
])
print(a.shape)
print(a)

# axis = 0  층
# axis = 1  행
# axis = 2  열

suml = a.sum(axis=0)
print(suml)
print(suml.shape)

sumr = a.sum(axis=1)
print(sumr)
print(sumr.shape)

sumv = a.sum(axis=2)
print(sumv)
print(sumv.shape)
