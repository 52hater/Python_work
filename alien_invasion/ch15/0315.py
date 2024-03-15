import matplotlib.pyplot as plt
# = from matplotlib import pyplot as plt

# x = range(4)
# y = [i**2 for i in x]

# plt.plot(x, y)
# plt.scatter(x, y)
# plt.hist(x)
# plt.show()

# import random

# # print([random.randint(0, 100) for _ in range(1000)]) # 어떻게 나오는지 한 번 보는거지
# x = [random.randint(0, 100) for _ in range(1000)] # from random import randint 임포트하면 random. 안써도 되지

# plt.hist(x)
# plt.show()

x1 = list(range(5))
y1 = [i**2 for i in x1]

x2 = list(range(5))
y2 = [i**3 for i in x2]

fig, ax = plt.subplots()
ax.plot(x1, y1, label="AAA", color="red", linewidth = 2)
ax.plot(x2, y2, label="BBB", color="black", linewidth = 2)
ax.scatter(x1, y1, color = 'green')
ax.scatter(x2, y2, color = 'orange')

ax.set_title('AAA vs BBB')
ax.set_xlabel('x1')
ax.set_ylabel('y1')

# ax.set_xticks(range(min(x1), max(x1)+1, 1))
# ax.set_yticks(range(0, 10, 1))

ax.set_xticks([0, 1, 2, 3, 4])

#from matplotlib.ticker import MultipleLocator, AutoMinorLocator
#ax.xaxis.set_major_locator(MultipleLocator(1))

plt.legend()
plt.show()
