prices = [10000, 20000, 30000, 40000]
# 20% 할인된 가격을 리스트로 만들어 출력하기. lambda를 이용하여

dis_prices = [
    (lambda p : p * 0.8)(p) for p in prices
]
print(dis_prices)