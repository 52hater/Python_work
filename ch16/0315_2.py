import datetime
from datetime import datetime as dt #as dt는 그냥 이름이 똑같으니까 헷갈려서 바꾼 것 # 아래에 데이터타입확인해보면 클래스이름과 모듈이름이 똑같아서 헷갈리는 걸 확인 가능
# 바꿨으니까 datetime.strptime('2024-03-15', '%Y-%m-%d') >> dt.strptime('2024-03-15', '%Y-%m-%d') 이렇게

# 백엔드 > 데이터타입과 친해져라 파싱등등

today = dt.strptime('2024-03-15', '%Y-%m-%d') # 파싱

print(today, type(today), type('2024-03-15')) # 타입을 항상 확인해봐 # 모듈이름이 데이트고 클래스이름도 또 데이트/'2024-03-15'는 str > 파싱

print(today + datetime.timedelta(days=3))