# import sys
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

# 출력
# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

N = int(input())
N_list = list(map(int, input().split())) #int함수가 무조건 먼저 나와야되네, 왜?  // 정수형으로 변환시켜주는 맵함수(?)
# 사용자가 입력한 값은 기본적으로 문자열 형태로 들어옴, 따라서 int 함수가 먼저 나오는 것은 사용자 입력값을 정수로 변환하는 과정이 리스트로 만드는 과정보다 먼저 이루어져야 하기 때문(순서대로!)
v = int(input())
print(N_list.count(v))

# # N과 N_list의 입력 개수가 동일해야한다고 생각하면
N = int(input()) 
N_list = input()
v = int(input())

if len(N_list.split()) == N :
    number_list = list(map(int, N_list.split()))

print(number_list.count(v))

#print('hello') # 왜 이게없으면
print(len('hello')) # 이게 안나오지 > 그냥 알수없는 에러인듯 신경ㄴ

# data = sys.stdin.readlines() #EOF
# data = [int(d.rstrip()) for d in sys.stdin.readlines()]
# print({int(d.rstrip()) for d in sys.stdin.readlines()}) # 문자열 ''로 나오던걸 정수형으로 덮어주고, \n 붙어서 나오던걸 rstrip으로 떼주기
# print(data.sort) # 얘를 만나고 난 후에는 원본이 유지가 안됨 **********
# print(sorted(data)) # 얘는 데이터를 그대로 놔둔 상태(원본이 살아있는 상태)에서 소트된거만 출력해줌 *********
# print('\n'.join(sorted(data))) # 데이타가 스트링일때 밑으로 떨어지게, int로 받았다면 string을 줘야겠지, \n 을 지워주고 ' ' 이렇게 하면 1 2 3 4 5 이런식으로 띄어쓰게 됨

# 메모리 > dump > file로 저장
# file > load > 메모리

# import json

# data = '{"name" : "Kim", "age" : 23}'
# member = {"name" : "Lee", "age" : 24}

# with open('member.json', 'w') as w_file:
#     json.dump(data, w_file)

# with open('member2.json', 'r') as r_file:
#     d = json.load(r_file)
#     print(d, type(d))

# d2 = json.dumps(member)
# print(d2, type(d2)) # str으로 빠짐 

# d3 = json.loads(d2)
# print(d3, type(d3), d3["name"]) # 딕셔너리로 바뀜

# import pickle

# with open('dump_member.json', 'wb') as w_file:
#     pickle.dump([1, 2, 3, 4, 5], w_file) # 로드해서 읽으면 이렇게 바로 쓸 수 있다