import matplotlib.pyplot as plt
import random

#x = list(range(100))
#y = list(range(100,200))

x = [random.randint(0, 100) for _ in range(100)] #0~99까지
y = [random.randint(100, 200) for _ in range(100)] #알트시프트화살표 > 복붙으로 위/아래로 가져오는

# x_walks = [5, -5]
# y_walks = [5, -5]

# x_data, y_data = [], []
# x, y = 0, 0
# x_data.append(x)
# y_data.append(y)
# for x_move, y_move in zip(x_walks, y_walks):
#     x, y = x+x_move, y+y_move
#     x_data.append(x)
#     y_data.append(y)


fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x[:50], y[:50], color='green') # 색깔을 반반으로 > 슬라이싱응용
ax.plot(x[50:], y[50:], color='yellow') # 색깔을 반반으로 > 슬라이싱응용
ax.scatter(x[:50], y[:50], color='red') # 색깔을 반반으로 > 슬라이싱응용
ax.scatter(x[50:], y[50:], color='blue')
plt.show()