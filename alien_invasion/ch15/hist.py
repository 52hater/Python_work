# 히스토그램

import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots()

data =[random.randint(0, 100) for _ in range(100)]

ax.hist(data)
plt.show()