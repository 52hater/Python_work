class Restaurant:
    def __init__(self, rname, rtype):
        self.restaurant_name = rname
        self.cuisine_type = rtype

    def describe_rastaurant(self):
        print(f"{self.restaurant_name}은 맛없어요")

    def open_restaurant(self):
        print(f"{self.cuisine_type}qwerqwerqwerqwer")

class IceCreamStand(Restaurant):#상속받아야하니까 레스토랑을 집어넣고
    def __init__(self, name, ctype, flavors):
        super().__init__(name, ctype)
        self.flavors = flavors
        
    def show_flavors(self): #함수정의할땐 무조건 셀프넣는다
        print("맛이 {}".format(self.flavors)) # 두개같은거
        print(f"맛이 {self.flavors}") # 두개같은거

new_rest = Restaurant()
ice_cream = IceCreamStand('Italy', 'pizza', '매운맛')
ice_cream.show_flavors()

my_restaurant = Restaurant('우리 중국집', '정통 이태리')
my_restaurant.describe_rastaurant()

print(f"{my_restaurant.restaurant_name}레스토랑은 오늘 영업은 합니다.")
print(f"{my_restaurant.restaurant_name}의 요리는 {my_restaurant.cuisine_type}방식을 고수합니다.")
