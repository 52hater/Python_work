for x in range(5):
    for y in range(10):
        print(x, y)

if x < 5:
    print('low')
else:
    print('high')

lst = [[1,2,3],[4,5,6]]
print(lst)
print(type(1))

d1 = {
    'a': {
        'aa': 1,
        'aa1': 2,
    },
    'b': {},
    'c': [],
    'e': range(10)
}
print(d1)

h = 'hello'
print(h)
print(h[0])
#h[0] = 'H' # 스트링타입은 못바꿔서?
#print(h)

db2 = {}
db2['a'] = list()
db2['a'].append('3') # db2 a라는데이터에다가 리스트를 넣고싶음(?)
db2['a'].append('왕훈')
db2['a'].append('A+')

db2['b'] = list()
db2['b'] = 3
print(db2)

db2['c'] = list() # 항상 리스트를 만들고나서 어펜드
db2['c'].append(3) # 이게 의도지
print(db2)

def add(a, b):
    return a+b
add(1, 2) # 함수호출
print(add(1,2))

data = {
    'a':1,
    'b':2
}
print(data)
add(**data)
add(data['a'], ['b']) #이렇게 하면 늘어날수록 개힘들겠지 > 윗줄처럼
print(add(**data))
print(add(data['a'], ['b'])d)

data = {'a':1, 'b':2, 'c':3}
data_idx = {v:k for k, v in data.items()} # 이렇게하면 양방향으로 할수있어서 많이 함

def pow2(n):
    return [x**2 for x in range(5) if x % 2 == 0] # 내가 필요한 데이터를 쉽게만들 수 있는 (제곱, 짝수 뭐 그런것까지) > 리스트 컴프리헨션(?) // 단점은 range(5)에서 5를 바꿀수가없어 > range(r)

def pow(n):
    lst=[]
    for x in range(5):
        if x % 2 == 0:
            lst.append(x**2)
    return lst

