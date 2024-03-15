N = int(input()) # 입력받은 숫자들의 개수를 뜻하는 변수 N
num = list(map(int, input().split()))
max_num = num[0]
min_num = num[0]

for i in range(0, len(num)): # 숫자들의 개수 N이나 list num의 길이 len(num)을 사용하면 될 듯?
    if (num[i] > max_num): # 인덱스는 몇번째인지니까 값 자체를 비교 > num[i]
        max_num = num[i]
    if(num[i] < min_num):
        min_num = num[i]
print(min_num, max_num)