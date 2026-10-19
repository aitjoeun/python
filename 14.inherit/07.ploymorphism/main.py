from programmer import Programmer
from famer import Famer
from actor import Actor

people = Programmer('김수철', 31, 'python')
people.introduce()
print('-' * 30)

people = Actor('박인술', 29, '왕과 사는 남자')
people.introduce()
print('-' * 30)

people = Famer('박광덕', 24, '오이')
people.introduce()
print('-' * 30)