class Car:
    """자동차 클래스"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 203000

    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름 반환"""
        lone_name = f"{self.year} {self.make}, {self.model}"
        return lone_name.title()
    
    def read_odometer(self):
        print(f"이 자동차의 주행거리는 {self.odometer_reading}")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_dodmeter(self, kilo_meters):
        """거리계 값을 주어진 값만큼 늘림"""
        self.odometer_reading += kilo_meters
    
my_new_car = Car('audi', 'a6', 2024)
my_used_car = Car('kia', 'K5', 2020)
print(my_new_car.get_descriptive_name)
my_new_car.odometer_reading = 204000 # 인스턴스 속성에 직접 접근해서 거리계 값을 직접 설정, my_new_car 인스턴스를 가져와 odometer_reading 속성을 찾고 그 값을 204000으로 수정
my_new_car.update_odometer(205000) # 업데이트메소드를 통해서 바꾼 것
my_new_car.read_odometer()

my_used_car