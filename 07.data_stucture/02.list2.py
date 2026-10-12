a = [1,2,3]

a[1] = ['a','b','c']
print(a)

print(a[0])
print(a[1])
print(a[1][0])

b = [1,2,3,4,5]
b[1:3] = [1000]
print(b)

b[1:2] = ['a','b','c']
print(b)