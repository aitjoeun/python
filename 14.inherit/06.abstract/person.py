# 추상클래스로 만들것임
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, job=None):
        self.name = name
        self.__age = age
        self.job = job

    def hello(self):
        print(f"Hello, I'm {self.name}")

    def update_age(self, age):
        if age < 0:
            print('나이는 음수일 수 없습니다')
        else:
            self.__age = age
            print(f'현재 나이는 {self.__age}세')

    def getAge(self):
        return self.__age

    @abstractmethod
    def introduce(self):
        pass
    