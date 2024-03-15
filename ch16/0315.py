# import pandas as pd
# pd.read_csv('sitka_weather_07-2021_simple.csv')

# with open ('./pcc_3e-main/chapter_16/the_csv_file_format/weather_data/pccsitka_weather_07-2021_simple.csv') as f:
#     for line in f:
#         print(line.rstrip().split(sep=','))

# import os
# os.path

# 453page

import csv
import matplotlib.pyplot as plt
from pathlib import Path # 리눅스 윈도우 그런 것 관계없이 사용가능(?)
from datetime import datetime as dt #as dt는 그냥 이름이 똑같으니까 헷갈려서 바꾼 것, 0315_2.py 가보면 데이터타입 보면서 확인

COL_DATE = 2 # 매직넘버는 빼놓고 상수니까 대문자로 표현 # 개발자는 매직넘버를 남겨두지 않는다
COL_TMAX = 4
x1, y1 = [], []
# 위에거가 더 간결하지
x2 = []
y2 = []

csv.reader('./pcc_3e-main/pcc_3e-main/chapter_16/the_csv_file_format/weather_data/sitka_weather_07-2021_simple.csv')

with open ('./pcc_3e-main/pcc_3e-main/chapter_16/the_csv_file_format/weather_data/sitka_weather_07-2021_simple.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        print(line, type(line))
        # x1.append(dt.strptime(line[COL_DATE], '%Y-%m-%d')) # 파싱해서
        # y1.append(int(line[COL_TMAX])) # 스트링으로 그대로 넣지않고 인트타입으로 바꿔서 넣으려면
        # 왜 오류가 나는지 확인

        x1.append(line[2])
        y1.append(line[4])

        x2.append(line[2])
        y2.append(line[5])

for idx, h in enumerate(header):
    print(idx, h)

# print(f'x: {x1}')
# print(f'y: {y1}')

plt.plot(x1, y1, label='TMAX')
plt.plot(x2, y2, label='TMIN')
plt.fill_between(x1, y1, y2, facecolor='pink', alpha=0.1)
plt.legend

# plt.xticks(rotation=90)
plt.show()
