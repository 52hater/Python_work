class Car:
    """자동차를 표현하는 클래스"""
    def __init__(self, make, model, year):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())