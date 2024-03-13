import matplotlib.pyplot as plt
# 숫자 조정해가면서 습득

x = list(range(1, 101)) # 100 ㄴㄴ
square = [i**2 for i in x] # 제곱함수
# square = lambda x: [i**2 for i in x]

fig, ax = plt.subplots()
#ax.plot(x, square, color = 'yellow')
ax.scatter(x, square, c=square, linewidth = 2, cmap=plt.cm.Blues)
ax.set_title('Square', fontsize=30)
ax.set_xlabel('X', fontsize=20)
ax.set_ylabel('Y', fontsize=20)
ax.tick_params(labelsize=10)
# ax.ticklabel_format(style='plain')
# plt.style.use('seaborn-v0_8-pastel') # ex)seaborn 스타일 + 버전붙여서
# for s in plt.style.available: # 터미널에 버전표시
#     print(s)
# ax.set_xlim(0,20)
# ax.set_ylim(0,20)
plt.colorbar()
plt.savefig('colorbar.png')
plt.show()