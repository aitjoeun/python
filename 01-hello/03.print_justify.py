# 5자리 확보 후, 왼쪽으로 붙이기
a = '{0:<5d}'.format(200)
print(a + '9')

# 5자리 확보 후, 오른쪽으로 붙이기
b = '{0:>5d}'.format(200)
print(b)

c = '{0:^5d}'.format(200)
print(c)

d = '{0:>05d}'.format(200)
print(d)