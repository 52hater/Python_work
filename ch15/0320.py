
from matplotlib import pyplot as plt

x= [1, 2, 3, 4]
print(type(x), x) # 한줄한줄 타입도 확인해
y = [i**2 for i in x]
print(type(y), y) # 한줄한줄 타입도 확인해
print(x, y) # 한줄짤때마다 프린트하는 습관, 막 30분 실컷짜고 프린트해보고 틀리면 문제가 큼

#plt.plot(x, y)
plt.scatter(x, y)
plt.show()