
from matplotlib import pyplot as plt

#import random 이렇게 해서 random.randint 해도되고
from random import randint #이 렇게 randint까지 임포트해도되고

# x = [(randint(0, 9) for _ in range(1000))]
# # print((randint(0, 9) for _ in range(100))) 이렇게 확인도 해보고

# plt.hist(x)
# plt.show()

x = list(range(1, 5))
y = [i*i for i in x]
#print(x, type(x))

plt.plot(x,y)
plt.title('X Square')
plt.xlabel('X')
plt.ylabel('X square')
plt.show()