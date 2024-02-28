print("Hello World!")

# a, b = input().split() # input 이거때문에 아래에 다 안나옴 입력받아야되는거라서
# a = int(a)
# b = int(b)
# a, b = (1, 2)
# print(a+b)

a1 = list()
b1 = []
type(a1), type(b1)
a1.append(1)
a1.append(2)
a1.append(3)
a1.append(4)
a1.append(5)
print(a1)

for i in range(1, 6):
    print(i)

for s in 'abcde':
    print(s)

type([1, 2, 3, 4, 5]), type((1, 2, 3, 4, 5)), type('abced'), type(range(5))

for i in range(1, 6):
    if (i % 2 == 0):
        print(i, '2')
    elif (i % 3 == 0):
        print(i, '3')
    else:
        print(i, 'even')
else: 
        print(i, 'odd')

a, b = input().split()
a, b = int(a), int(b)
if (a > b):
     print('>')
elif (a < b):
     print('<')
else:
     print('==')

scores = input("점수를 입력하세요 : ").split() # 여러 개의 점수를 리스트로 입력 받음
scores = [int(score) for score in scores] # 각 점수를 정수로 변환

for score in scores:
     if (score >= 90):
          print('A')
     elif (score >= 80):
          print('B')
     elif (score >= 70):
          print('C')
     elif (score >= 60):
          print('D')
     else:
          print('F')

score = input("당신의 점수는 : ")
score = (int(score))
if (score >= 90):
     print('A')
elif (score >= 80):
     print('B')
elif (score >= 70):
     print('C')
elif (score >= 60):
     print('D')
else:
     print('F')