# 함수의 매개변수로 함수 전달하기
def ten_times(func):
    for i in range(5):
        func()

def print_hello():
    print("hello")

ten_times(print_hello) #함수를 전달하는데 파라미터는 전달안했음

def print_work():
    print('coding')

ten_times(print_work)

def minus(x,y):
    return x-y

def add(x,y):
    return x - y

def apply_opperation(operation, x, y): #파라미터까지 전달하고싶어 ###map함수
    return operation(x,y)

result = apply_opperation(add, 3, 4)
result2 = apply_opperation(minus, 3, 4) # 마이너스를 던져줘
print(f"add 결과 = {result}, minus 결과 = {result2}")

###map(), filter() 함수 사용

# def power(item):
#     return item * item

# def under_three(item):
#     return item < 3

power = lambda x: x * x # 함수대신 람다식을 이용
under_three = lambda x: x < 3

lst = [1, 2, 3, 4, 5]
map_list = map(power, lst)# 위에 어플라이 저걸 안해도 맵을 쓰면 간단하게 코딩
print(f"map() 함수 적용결과 : {list(map_list)}")

filter_list = filter(under_three, lst)
print(f"filter() 함수 적용결과 : {list(filter_list)}")#필터를 3보다 작은거를 적용 한 것
# 조건에 맞는거만
# 이거보다 간단한게 람다식

# 함수를 맨첨에 전달, 어플라이, 맵함수 필터함수, 람다식
# 나중에 머신러닝 딥러닝 관련, 구글링으로 복습 철저

