#데이터분석>데이터의시각화
from matplotlib import pyplot as plt
import csv
from datetime import datetime as dt

x1, y1 = [], []
x2, y2 = [], []

with open('./ch16/weather.csv', 'r') as f: # 'r'은 읽기전용
    reader = csv.reader(f)
    header = next(reader)
    print(header)


    for row in reader:
        # print(type(dt.strptime(row[2]), '%Y-%m-%d')), type(int(row[4]), type(int(row[5])))
        x1.append(dt.strptime(row[2],"%Y-%m-%d"))
        y1.append(row[4])
        y2.append(row[5])

plt.plot(x1, y1, label='TMAX', color='red')
plt.plot(x1, y2, label='TMIN', color='blue')
#x2 비어있다는데?
plt.fill_between(x1, y1, y2, alpha=0.5)
plt.xticks(x1, rotation = 'vertical')

plt.xlabel('Date')
plt.legend()
plt.show()

