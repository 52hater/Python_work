def test():
    return (10,20)

a,b = test() # tuple 값을 리턴
print(f"a = {a}, b = {b}") # 무식하게 print(a) print(b) 이렇게 하지말래
lst = ['a', 'b', 'c', 'd']
for i, value in enumerate(lst): # 리스트가 주어지면 인덱스와 값을준다(enumerate함수())>리턴값이 튜플>>enumerate()가 튜플을 리턴한다
    print(f"i = {i}, value = {value}")#0123 찍고 값 주고(ctrl f5해보면 터미널에)

def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name")
    f_name = input("First name : ")
    if f_name == 'q':
        break # 루프(무한루프) 빠져나오는거
    l_name = input("Last name : ")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")