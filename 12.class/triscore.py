class Triangle:
    def getArea(self, b, h):
        self.b1 = b
        self.h1 = h
        return self.b1 * self.h1 / 2

class Score:
    def set(self):
        self.name = input('이름 입력 : ')
        self.python = int(input('파이썬 점수 입력 : '))
        self.ai = int(input('인공지능 점수 입력 : '))
        self.sum = self.python + self.ai
        self.avg = self.sum / 2

    def output(self):
        print('이름 : ', self.name)
        print('파이썬 점수 : ', self.python)
        print('인공지능 점수 : ', self.ai)
        print('합계 : ', self.sum)
        print('평균 : ', self.avg)