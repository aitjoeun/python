'''
* set : 중복불가,
        순서가 없다(index 없음)
        {중괄호 사용}

    *** 주의 : 빈 set을 만들때 {} 이건 딕셔너리
        set() -> 만들어야 set이 됨
'''
a = {1,2,3,1,2,3,4,1,3,5}
print(a)
print(len(a))

b = {'홍길동', 3, 5, True, (4,5)}
print(b)

c = {}
print(type(c), c)

d = set()
print(type(d), d)