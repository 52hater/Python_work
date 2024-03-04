def make_sandwich(*toppings):
    """샌드위치 토핑 추가하는 함수"""
    print("\n토핑을 추가해 주세요")
    for topping in toppings:
        print(f"{topping}(을/를) 추가합니다")
    print("샌드위치가 완성되었습니다")

make_sandwich('슬라이스햄', '크림치즈', '머스타드', '양배추')
make_sandwich('슬라이스햄', '양상추', '체다치즈')
make_sandwich('달걀후라이', '딸기잼', '모짜렐라치즈')