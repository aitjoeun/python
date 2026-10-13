a = [1,2,3,4,5,1,3,2]
b = (6,7,8,9,10)
c = {11,12,13,14,15}

# list() : 리스트로 변환
# set() : set으로 변환
# tuple() : 튜플로 변환
set1 = set(a)
print(a)
print(type(set1), set1)

tuple1 = tuple(a)
print(type(tuple1), tuple1)

list1 = list(b)
print(type(list1), list1)