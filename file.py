with open('name.txt', encoding='utf-8') as file:
    for line in file:
        print(line)
        print(line.rstrip()) # 오른쪽의 꼬다리 잘라서 처리하는거
        print(file.readlines())
        for line in file.readlines():
            print(line.rstrup())

def add(a, b):
    return a+b
print(add(1, 2))

# def add(c=5, d=8):
#     print(add(c, d)) # 왜 안돼

print('A', end='') # 디폴트는 end='\n' 숨어있음
print('B', end=' ')
print('C')
print('D')
print('A', 'B', 'C', sep=', ')

# import csv

# with open('grade.csv') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     for line in reader:
#         print(line)
#     print(header)

n = range(5) #레인지:클래스
print(n)

r = iter(n)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

for i in range(5):#for 문 종료 스탑이터레이션으로 에러
    print(i)