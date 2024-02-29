#출력할 디자인이 저장된 리스트
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

#남은 게 없을 때까지 디자인을 출렧합니다
#출력한 디자인을 completed_models로 옮깁니다
def print_models(unprinted_designs, completed_models): #리스트가 파라미터면 뮤터블
    """빈 리스트일때까지 출력"""
while unprinted_designs: # 빈 리스트면 false가 됨
    current_design = unprinted_designs.pop() # 한개씩 삭제
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

#완료된 디자인을 표시합니다
def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_models)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def modify_string(s):# 스트링 값을 전달받았음
    # immutable 변수는 튜플, 숫자, 스트링, 불리언 이런것들
    s = s + "world" # 근데 이제 변경이 안됐음>임뮤터블 
    print(s) # 함수에서는 헬로월드고 함수 마치고나서는 헬로 # 변수 s는 원래 변수가 가리키는 주소와 다른 것

st = "hello "
modify_string(st)
print(st) # 실행하면 월드는 안나오고 헬로만 출력됨 > 변경안됨