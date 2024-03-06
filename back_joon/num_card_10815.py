N, M = int(input())
n_card = list(map(int, input().split()))
m_card = list(map(int, input().split()))

dic = {}

for o in m_card:
    dic[o] = 0

for c in n_card:
    if c in dic:
        dic[c] = 1

for d in dic:
    print(dic[d], end=' ')