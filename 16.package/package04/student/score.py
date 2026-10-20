# *args => 튜플로 반환
# def average(*scores):
#     return sum(scores) / len(scores)

# **kwargs => 딕셔너리로 반환
def average(**scores):
    total = 0

    for subject, score in scores.items():
        print(f'{subject} : {score}점')
        total += score

    return total / len(scores)