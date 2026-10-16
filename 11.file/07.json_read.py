import json

# encoding 함수정의
def enco(file_path):
    encodings = ['UTF-8', 'EUC-KR', 'CP949']

    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return enc
        except UnicodeDecodeError:
            continue

#  data.json 한개의 {}만 있을 때
files = '11.file/data/data.json'
with open(files, 'r', encoding=enco(files)) as f:
    data = json.load(f)

print(data)
print(type(data))

print(f'이름 : {data['name']}')
print(f'보유기술 : {data['skills']}')
print(f'보유기술 : {data['skills'][0]}')

#  data2.json 여러개의 {}가 있을 때
files = '11.file/data/data2.json'
with open(files, 'r', encoding=enco(files)) as f:
    
