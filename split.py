# a, b = input().split() # split 함수를 호출, input함수의 리턴타입은 String
# a ,b = int(a), int(b)
# print(a+b)

# def get_string():
#     return '1 2'

# a, b = get_string().split()
# # print(a*b)

# print(type(get_string))

# # '1 2' # 입력을 받음 문자열을 입력받을 수 있음
a, b = input().split()
a, b = s.split() #'1' '2' # 입력된 문자열을 공백을 기준으로 나누어 리스트 형태로 저장하고, 그 값을 변수 a와 b에 할당함
# 위 두 줄의 코드는 '1 2'와 같은 문자열을 입력받았을 때, 리스트 ['1', '2']를 생성하고 변수 a에 '1', 변수 b에 '2'를 할당함
a, b = int(a), int(b) # 1 2 
# 변수 a와 b에 할당된 값을 정수형으로 변환하여 다시 변수 a와 b에 할당함
# 위 코드는 변수 a와 b에 할당된 값 '1'과 '2'를 정수형으로 변환하여 다시 변수 a와 b에 각각 할당함
a, b = int('1'), int('2') # a와 b값 출력
print(a, b)
# 변수 a와 b에는 각각 정수형으로 변환된 값이 할당되어 있으므로, 이를 출력하면 '1 2'가 출력됨

# n = int(input())
# S = 0
# for i in range(1, N+1):
#     S += i
# print(S)