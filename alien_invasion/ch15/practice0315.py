# 이름   국어 영어
# 홍길동 50   30
# 이순신 70   50
# 강감찬 20   70

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

names = ['홍길동', '이순신', '강감찬']
subjects = ['국어', '영어']
scores = [[50,30], [70,50], [20, 70]]

ax.set_xlabel('Name')
ax.set_ylabel('Score')

bar_width = 0.35

#x축에 이름설정
ax.set_xticks([i + bar_width / 2 for i in range(len(names))])
ax.set_xticklabels(names)

for i, name in enumerate(names):
    x = [j + i * bar_width for j in range(len(subjects))]  # 각 사람마다 x 좌표 설정
    ax.bar(x, scores[i], width=bar_width, label=name)

# index = 0
# for name in names:
#     x = [j + index * bar_width for j in range(len(subjects))]  # 각 사람마다 x 좌표 설정
#     ax.bar(x, scores[index], width=bar_width, label=name)
#     index += 1

#ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_yticks(range(0, 100, 10))

ax.legend()
plt.show()