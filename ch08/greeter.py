def greet_user(username): # def = 함수정의 키워드 / greet_user = 함수명 / 스트링은 immutable(불변하는) 변수
    """단순한 인사말을 표시합니다""" #다큐먼트스트링 = 함수가 수행하는 작업 설명하는 주석
    print(f"Hello, {username.title()}") # 타이틀다음에 ()를 빼먹었었네, 함수니까 ()를 붙여야지
    username = 'park'

input_name = 'wang'
greet_user(input_name) # 함수호출
input_name = 'kim' # 값이 변경되는 것이 아니라 변수를 하나 더? 다시? 설정하는 것
greet_user(input_name) # 그래서 헬로킴도 하나 나옴
#help(greet_user) # 다큐먼트스트링(독스트링)을 출력해줌
#print(greet_user.__doc__) # 독스트링 출력