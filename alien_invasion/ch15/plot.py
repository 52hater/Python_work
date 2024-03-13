import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x1 = [1, 2, 3, 4]
y1 = [2, 3, 4, 6]
ax.scatter(x1, y1, label='blue')

x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]
ax.scatter(x2, y2, label='yellow')

ax.set_title('Plot A and B')
ax.set_aspect('equal')
ax.set_xlabel('Age')
ax.set_ylabel('BMI')
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.legend() # 범례(?) > 오른쪽 위에
ax.grid()
plt.savefig('plot.png') # 저장
plt.show()