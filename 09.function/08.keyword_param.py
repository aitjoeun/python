# 키워드 인자
def display_info(academy, name, classroom):
    print(f'Academy : {academy}, Name : {name}, ClassRoom : {classroom}')

display_info('더조은', '이승우', '704호')

def display_info2(name, classroom, academy='더조은'):
    print(f'Name : {name}, ClassRoom : {classroom}, Academy : {academy}')

display_info2('한수철','303호')

# 순서와 무관하게 나오게 하려면
display_info2(classroom='703호', name='박미화', academy='한샘')