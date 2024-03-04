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
        print(f"이 자동차의 주행거리는 {self.odometer_reading}kilometers on it.")

    def update_odometer(self, mileage):
        """거리계를 주어진 값으로 설정"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_dodmeter(self, kilo_meters):
        """거리계 값을 주어진 값만큼 늘림"""
        self.odometer_reading += kilo_meters

class Battery:
    """배터리"""
    def __init__(self, battery_40 = 40):
        """배터리 속성 초기화"""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리의 크기를 설명"""
        print(f"이 차는 {self.battery_size}KWh의 배터리 내장됨")

class Electric_car(Car):
    """전기차"""
    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화
        그리고 전기차에만 해당하는 속성을 초기화"""
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def describe_battery(self):
        """배터리의 크기를 출력"""
        return(f"이 차의 배터리 용량은 {self.battery_size}KWh 입니다.")

    def get_descriptive_name(self): #Car에 이게 있잖아 #override 확인?
        print(super().get_descriptive_name())
        print(f"차량 배터리 크기는 {self.battery_size}")

my_ionic = Electric_car('현대', 'ionic6', 2024, 3000)
print(my_ionic.get_descriptive_name())
my_ionic.battery.describe_battery()
print(f"배터리 크기는 {my_ionic.describe_battery()}")
my_ionic.describe_battery()
my_car = Car('Benz', 'E200', '2023')
print(f"차 제원은 {my_car.get_descriptive_name()}")