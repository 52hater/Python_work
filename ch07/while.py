n = 0
while n < 21:
    print(n)
    n += 1

print(type(n < 2))

# while True:
#     print(n)
#     n += 1
#     if n == 3:
#         break

from pickle import TRUE
n = 0
b_N = True
while b_N:
    print(n)
    n += 1
    if n == 5:
        break

        # while 루프는 무한루프나 한번도 실행안되는걸 조심

a = [1,2,3]
b = []
for i in a:
    b.append(i)
    del a[0]
    print(a, b)

a = [1,2,3]
b = []
N = len(a)
for _ in range(N): #a가 자꾸 바뀌니까 인덱스를 쓸 수가 없다 > 팝을 쓰는 이유
    p = a.pop()
    b.append(p)
    print(a, b)

a = [1,2,3]
b = []
N = len(a)
for _ in range(3):
    # p = a.pop()
    b.append(a[-1])
    del a[-1] # 이거 주석하면 팝
    print(a, b)

a = [1,2,3] # 1,2,3을 b로 옮겨 while로
b = []
while N == 0:
    p = a.pop()
    b.append(p)
    N -= 1
    print(a, b)

a = [1,2,3] # 1,2,3을 b로 옮겨 while로
b = []
while True:
    if a == []: break
    p = a.pop()
    b.append(p)
    print(a, b)

a = [1,2,3] # 위에 코드 살짝 변형한거지
b = []
while True:
    if not a: break
    p = a.pop()
    b.append(p)
    print(a, b)

a = [1,2,3] # 위에 코드 살짝 변형한거지
b = []
while a:
    p = a.pop()
    b.append(p)
    print(a, b)

a = [1,2,3]
a.remove(2)
print(a)

d1 = {}
d1['왕훈'] = list(map(int, input().split())) #인트:람다함수, 맵:객체 // 들어온데이터를 맵으로 변형, 인트>문자열인게 정수로 싹 바뀌게, 스플릿은? ->
print(d1) # 터미널에서 1 2 3 4 5 입력하면 {}'왕훈' : [1, 2, 3, 4, 5]} 출력

#data 1.변형 > map(f, data) / 2.조건 > filter(f2, data) / 3.줄인다 > reduce(f, data)

data = list(range(1, 11)) # 위에 왕훈리스트를 터미널에 쳐서 완성시켜야 실행됨
print(data)
square = lambda x: x**2
print(square(2))
#맵 필터 리듀스
even = lambda x: x%2==0
print(list(map(square, data))) # 10개로 나옴
print(list(filter(even, data)))
from functools import reduce
add = lambda a, b: a+b
print(reduce(add, data))

