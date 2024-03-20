import json
import plotly.express as px

#json load : csv처럼 파일을 읽
#json loads : str->dict / dict->str

#160개
mag, lat, lon = [], [], []

with open('./eq.geojson', 'r', encoding='utf-8') as f: # r = 읽기전용
    data = json.load(f)
    print(type(data), data['type'], type(data['metadata']['count']), type(data['features'])) # 생긴것 자체가 제이슨이 딕셔너리랑 잘 맞음 / 딕셔너리니까 키값으로 접근할 수 있지 / 제일왼쪽:타입 ~~~ ...
    #딕셔너리는 type(data['metadata']['count']) 보니까 int로 인식해주네 // json파일을 보면서 비교대조해봐
    
    for feature in data['features']: #data['features']가 리스트니까
        print(data['features'][0]['properties']['mag']) # 이런식으로 보고 원하는 데이터를 뽑을 수 있어야 됨 (책 465~468 p)
         # 플롯이 나오는지 확인해보고 (데이터타입 확인)
        mag.append(feature['properties']['mag'])
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])
        print(data['features'][0]['geometry']['coordinates']) # features > 리스트니까 그걸 x1=[] y1=[] 이런식으로 받을까? > 근데 지도니까 mag, (lat, lon) 위도경도 > 각각 나눠서 담아보자

fig = px.scatter_geo(lat=lat, lon=lon, size=mag)
fig.show()
