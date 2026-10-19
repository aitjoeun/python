'''
은행 : 개설할 때 계좌주 이름과 초기 예금액을 넣어줌
        입금하면 잔고 변경
        출금 잔고 변경(찾는금액 잔액보다 많으면 출금안되게 출력'잔액부족')

        [???님의 계좌 정보] (현재 잔액 : ???원)
'''
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f'{self.owner}님의 계좌가 개설되었습니다. 현재잔액은 {self.balance}원')
    
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount}원이 입금되었습니다.')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액이 부족합니다')

    def __str__(self):
        return f'[{self.owner}님의 계좌 정보] 현재 잔액 : {self.balance}원'
    

b1 = BankAccount('홍길동', 10000)
b2 = BankAccount('김철수')
b1.withdraw(20000)
b2.deposit(20000)

b1.deposit(20000)
b1.withdraw(15000)
b2.withdraw(10000)
print(b1)
print(b2)