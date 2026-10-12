# 04.if_else.py

jumsu = 81

if jumsu >= 90 :     # 90보다 큰값은 모두 다
    print('A학점')
else :              # 90미만인 모든 값(72,67,0, -5, -7)
    if jumsu >= 80:  # 90미만 ~ 80이상(80~89)
        print('B학점')
    else :
        if jumsu >= 70:
            print('C학점')
        else :
            if jumsu >= 60:
                print('D학점')
            else:
                print('F학점')

if jumsu >= 90:
    print('A학점')
elif jumsu >= 80:
    print('B학점')
elif jumsu >= 70:
    print('C학점')
elif jumsu >= 60:
    print('D학점')
else:
    print('F학점')