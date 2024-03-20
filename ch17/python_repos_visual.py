#파이썬 도큐먼트에서 추천해주는 리퀘스트로//하이어 레벨 > 사람에 가까운
#name을 x축에, stargazers_count를 y 축에
# 488 ~ 489p 참고 
# 키로 접근
import matplotlib.pyplot as plt
import requests
import json

names, stars = [], []

# 파일로 쓰면 이렇게 쓰는데 어떻게 고쳐야하지 url을 쓰면 (아래)
# with open('https://api.github.com/search/repositories?q=language:python+sort:stars', 'r', encoding = 'utf = 8') as f:
#     res = json.load(f)
#     print(len(res['items']), type(res['items']))
#     for item in res['items']:
#         print(item['name'], type(item['name']))
#         print(item['stargazers_count'], type(item['stargazers_count']))
#         names.append(item['name'])
#         stars.append(item['stargazers_count'])

# plt.bar(names, stars)
# plt.xticks(rotation=45)
# plt.show()

# 이렇게? 아닌것같은데
url = 'https://api.github.com/search/repositories?q=language:python+sort:stars'
response = requests.get(url)
print(len(response['items']), type(response['items']))
for item in response['items']:
    print(item['name'], type(item['name']))
    print(item['stargazers_count'], type(item['stargazers_count']))
    names.append(item['name'])
    stars.append(item['stargazers_count'])

plt.bar(names, stars)
plt.xticks(rotation=45)
plt.show()




# print(requests.get(u)) # 리스폰스 200

# #res 저장
# #req 보낼때

# res = requests.get(u)
# print(res.json())
# print(type(res.json()))