
from matplotlib import pyplot as plt

from random import randint

#f2로 변수들 이름 한꺼번에 바꾸는 것
#alt shift 화살표로 복사해오는 것

x1 = list(range(1, 5))
y1 = [i*i for i in x1]

x2 = list(range(1, 5))
y2 = [i**3 for i in x2]

fig, axs = plt.subplots(1, 2, figsize=(10, 7))
# 하얀색 도화지는 fig, ax는 축

axs[0].plot(x1, y1, label='A', color='red')
axs[0].plot(x2, y2, label='B', color='blue')

axs[1].scatter(x1, y1, label='A', color='red')
axs[1].scatter(x2, y2, label='B', color='blue')


# plt.plot(x1, y1, label='A', color='red')
# plt.plot(x2, y2, label='B', color='blue')

plt.title('X Square')
plt.xlabel('X')
plt.ylabel('X square')
plt.legend()
plt.show()