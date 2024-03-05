from car import Car #클래스를 가져옴, 함수도 마찬가지겠지, car는 파일 Car는 클래스

my_new_car = Car('audi', 'a6', 2024)
print(my_new_car.get_descriptive_name)
my_new_car.odometer_reading = 204000
my_new_car.update_odometer(205000)
my_new_car.read_odometer()

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