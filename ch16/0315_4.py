
import json
# 1. json - dump, load <--- 일반적인 상황은 아니고 file을 쓰는 // 파일을 배우고있으니까 일단 하는
# 2. json - dumps, loads <- fast API, Flask // 일반적인 상황

data = {"name" : "Kim", "age" : 23}

print(data["name"], type(data), json.dumps(data), type(json.dumps(data))) # 타입은 확인위해 자꾸 찍어보는 것, 나중엔 지워야지 //스트링으로 바뀌면 성공한 것
# json.dumps(data) 요렇게 스트링을 받으면  json.loads(json.dumps(data))를 하면 얘의 타입은 이제 ?
# 브라우저 <-> 서버 / 스트링