# arr = [int(input(a%42)) for _ in range(10)]

arr = []
for _ in range(10):
    num = int (input())
    arr.append(num%42)

arr = set(arr)
print(len(arr)) # 개수len

# 입력을 한줄에 다 받으려면
# arr = []
# input_string = input("Enter 10 numbers separated by space: ")
# # 공백으로 구분된 숫자들을 리스트로 변환
# numbers = input_string.split()
# for num in numbers:
#     arr.append(int(num)%42)

# arr = set(arr)
# print(len(arr))

# 교수님풀이 // 모듈화연산 //
data = [int(input()) % 42 for _ in range(10)]
print(len(set(data)))

# answer = []
# for d in data:
#     if d not in answer:
#         answer.append(d)
