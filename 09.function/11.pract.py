'''
문1) 카페 주문
메뉴와 사이즈 2개를 입력받음.
만약 사이즈가 입력이 안되서 무조건 small 사이즈임

문2) 택배 배송정보
받는사람, 주소, 전화번호를 입력받음.
순서와 상관없이 받아서 출력

문3) 친구들과 식당에 가서 각자 낸 금액의 합계 구하기(tuple)
친구들이 갈 때마다 인원이 달라짐

문4) 회원가입 정보를 입력받기(dict)
사람마다 입력하는 정보의 개수가 다를 수 있음
'''

# 문1
def order_coffee(menu, size='small'):
    print(f'{menu} | {size} 사이즈 주문')

order_coffee('아메리카노')
order_coffee('카페라떼', 'large')
print('-'*30)

# 문2
def delivery(name, address, phone):
    print('받는 사람 :', name)
    print('주소 :', address)
    print('전화번호 :', phone)

delivery(phone='010-1234-1234', name='김철수', address='서울 강남')
print('-'*30)

# 문3
def cal_bill(*money):
    total = 0
    for price in money:
        total += price
    return total

print(cal_bill([13000, 9000]))
print(cal_bill(13000, 9000, 15000, 12000))
print('-'*30)

# 문4
def signup(**info):
    print('회원가입 정보')

    for k, v in info.items():
        print(k, ':', v)

signup(
    name='이상원',
    age=25,
    email='abc@test.com'
)

signup(
    name='홍말숙',
    age=23,
    email='abcd@test.com',
    city='인천'
)