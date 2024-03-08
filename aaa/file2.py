import os

from pathlib import Path

dir_path = Path ('/aaa')
print(dir_path)

file_path = Path('/aaa/a/txt')
print(file_path)

print(os.path.isdir(dir_path))
print(os.path.isdir(file_path))

for d in os.listdir():
    print(d, os.path.isdir(d))
    if '.txt' in d:
        print('FOUND!')

no_file = Path ('./aaa/b.txt')
print(os.path.exists(no_file))
print(os.path.exists(file_path))

print(os.path.split(Path('/aaa/b.txt')))
print(['.', 'aaa', 'b.txt'])
print(Path('aaa', 'b.txt'))

path = Path ('/aaa/aa.txt')

with open(path, 'w') as file: # aa파일이 없음,,,'w':쓰겠다
    file.write('a\n')
    file.write('aa\n')
    file.write('aaa\n') # 왜 안생기지 > 위에 주석처리하면 됨 > 뭐떄문에 안됐던건지?

path = Path ('/aaa/aaa.txt')
if path.exists(): # 안전장치(?) 파일이 없으면 에러가 나니까
    with open(path) as file:
        for line in file:
            print(line)

path = Path ('/aaa/aaa.txt')
try:  # 일반적인 상황에서는 반드시 해라
    with open(path) as file:
        for line in file:
            print(line)

except Exception as e:
    pass
print(e)

import json
print(type(json.loads(['foo', {'bar' : ('baz', None, 1.0, 2)}])))
print(type(json.dumps({'4':5, '6':7})))
print(type(json.load({'4':5, '6':7})))

data = json()
type(data) # json

data = json.parse("{'name':'kim', 'age':22}")
type(data) #json
print(data.name) #1
print(data.age) #2