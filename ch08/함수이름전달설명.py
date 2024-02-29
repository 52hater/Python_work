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

def apply_opperation(operation, x, y): #파라미터까지 전달하고싶어
    return operation(x,y)

result = apply_opperation(add, 3, 4)
result = apply_opperation(minus, 3, 4) # 마이너스를 던져줘