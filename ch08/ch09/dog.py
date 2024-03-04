class Dog: # 클래스이름은 대문자로시작
    """개 클래스"""
    def __init__(self, name, age): # 셀프는 뭔데? -> 생성된 객체 자기자신
        # 생성자 init에 속성(자바에서의 클래스 필드에 해당)
        """name과 age 필드 초기화"""
        self.name = name
        self.age = age
        self.price = 100
    
    def sit(self):
        """앉기"""
        print(f"{self.name} is now sitting.")

    def roll_over(self): # ***** 클래스 내에서 접근할떄는 self. (습관!) *****
        """구르기"""
        print(f"{self.name} rolled over!")

    # def get_price(self):
    #     """개의 가격 반환"""
    #     return self.__price

my_dog = Dog('Willie', 6) # 생성자 호출(파이썬은 생성자가 따로 없음) > 인스턴스 생성 > __init__()함수가 자동 호출 , (마이도그가 변수고 도그객체를 갖고있다)
# 파라미터가 전달돼서 도그객체를 만들었어, 생성된 객체 자기자신:셀프, 셀프(리시브 오브젝트)를 마이도그라는 변수가 가리키는
# __init__()의 언더라인 : 특별한표기법(229p)
my_dog.sit() #변수.메소드 근데 sit단에 파라미터전달하는게 없어 > 위에는 있는데? > ㄴㄴ sit의 셀프는 my_dog를 가리키는 것
# 모든클래스의 메소드는 self를 포함하고있어 my_dog는 셀프야. 수신객체 리시브오브젝트
#셀프:만들어진객체를 가리킴, 메소드 호출할땐 셀프가 만들어진 객체my_dog를 가리킴
print(f"개 이름은 {my_dog.name} 개 가격은 {my_dog.price} 개 나이는 {my_dog.age}") # ***** 클래스 밖에서 접근할 때에는 변수.(인스턴스.) !! *****
# __price는 클래스 내부에서만 접근 가능한 private 변수 > 클래스 외부에서 해당 변수에 접근하려고 할 때는 메소드를 통해 간접적으로 접근해야 합니다.
# 보통은 이러한 변수에 접근할 수 있는 getter와 setter 메소드를 제공합니다. getter 메소드를 통해 값을 반환하고, setter 메소드를 통해 값을 설정합니다.
# 따라서 __price 변수에 접근하려면 이에 해당하는 getter 메소드를 정의해야 합니다


#__price관련된거는 아직 해결안됨

your_dog = Dog('Lucy', 3)
your_dog.sit()
your_dog.price = 200
print(f"{your_dog.name}는 {your_dog.price}원 짜리야")