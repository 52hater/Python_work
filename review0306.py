a, b = {}, []
type(a), type(b)
print(type(a))
print(type(b))

a = {'a':1,'b':2,'c':3} # 키값은 unique
b = [1,2,3]

print(a['b'])
print(b[1])

data = {'정원':'A+', '윤정':'A+', '세영':'A+'}
data = {9:[9, '철수', 'A+'], 7:[7, '영희', 'C0'], 3:[3, '찰스', 'B+']}
print(data[9])
print(data.get(7))

print(sorted(data))
print(sorted(data.items()))

first = lambda x: x[0]
second = lambda x: x[1]
for row in data.items():
    print(first(row), second(row))

print(sorted(data.items(), key=second))
print(sorted(data.items(), key=lambda x: x[1].reverse))#성적이 낮은순으로 소팅(reverse)

for row in data.items(): #보통 .items() 를 잘 까먹음 > 순회
    print(row, type(row))

for k, v in data.items(): #키 벨류
    print(k, v, type(row))

if 4 in data:
    data[4]
    print(data.get(4))
    print(data.get(4, 0))

e = [3,2,1]

e.sort()

sorted(e)

print(sorted(e))


