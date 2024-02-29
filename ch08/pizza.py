def make_pizza(size, *toppings):#함수를 먼저 정해놓고  #tuple로 받은 것 #사이즈고정 토핑가변
    """주문 요약"""
    print(f"making {size}-inch pizza 다음 토핑으로")
    for topping in toppings:#리스트에있는애들을 하나씩 출력
        print(f" - {topping}")

make_pizza('pepperoni')#파라미터하나
make_pizza('mushroom', 'green pepper', 'extra cheese')#파라미터세개