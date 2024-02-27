for value in range(1, 5):
    print(value)

for value in range(6) :
    print(value)
    numbers = list(range(1,10,2)) #3번째 2는 step
    print(numbers)
    number_set = {}

    squares = [] # 리스트변수
    for value in range(1,11) : #콜론 = 블럭의 시작 / value가 for문에 있는 변수
        #squares.append(square) #squares = list변수
        squares.append(value ** 2)

    print(squares)
    print(value)

squares = [value**2 for value in range(1, 11)]
#squares리스트를 만드는데 알맹이를 for문으로 작성한다 = list comprehension(이해하다) 리스트내포/치환문쓰고 for문으로 작성한거/ 위의 3줄을 간단하게 표현 한 것
print(squares)
print(squares[-3:]) #slicing

a = [1,2]
b = [3,4]
c = a + b
print(c)

#c = a - b #에러
c1 = [x for x in a if x not in b]
c2 = list(set(a)-set(b))
print(c1)
print(c2)

b = [0]
c3 = b*5
print(c3)

a = [10, 20, 30, 40, 50]
# b = a # Shallow copy # 주소를 복사하는거니까 a의 값이 변경되면 같이 바뀜(주소를 복사한거니까)
b = a[:] # deep copy # 값을 변경해도 원래 카피대로(값을 복사한거니까)(새로운 메모리에 카피해서 저장)
a[0] = 100
print(b)

a = [[1,2,3],[4,5,6]]
b = a[:] #shallow copy #???????뭐야이거
print(b)
a[0][0] = 100
print(b)

# shallow copy, deep copy 새로 찾아서 공부

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # deep copy -> my_foods만 변경이 되고 friend_foods는 변경이 안됨
# friend_foods = my_foods # shallow copy
my_foods.append('cannoli')

print("My favorite foods are : ")
print(my_foods)

print("\nMy friend's favorite foods are : ")
print(friend_foods)

dimensions = (10,20,30,40,50)
# dimensions[0] = 30 # 요거는 리스트니까 에러남
print(dimensions)
for dimension in dimensions:
    if dimension  >= 20:
        print(dimension)
dimensions = (200,50) # 116p, 얼마든지 덮어쓰기로 재정의해서 쓸 수 있다
print(dimensions)