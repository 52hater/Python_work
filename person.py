class Person:
    count = 0 ### 클래스변수*****//클래스필드 > person객체들이 공유한다
    def __init__(self, name, age, address): # init:생성자역할, 그럼 소멸자는? 14번째 줄 __del__()
        self.name = name ### 인스턴스 변수 > 함수내에 있음*****
        self.age = age
        self.address = address
        self.weight = [65,66,67,68] # 파라미터 안넘겨줌, 공개속성
        self.height = 180
        self.__vision = 1.0 # private 속성
        print("{}객체가 생성됨".format(self.name))
        Person.count += 1 ###클래스변수를 증가시키는거지 > 바로 못갖다쓰네? > 클래스이름을 앞에다가 > 클래스명.count //메소드 안에서 쓰여
    @classmethod ## 자바에서의 어노테이션 > 파이썬에서는 decorator
    def printing(cls):#cls:클래스 / cls라는 변수를 써야함 self를 고정으로 쓰듯이 
        print("객체수는 {}".format(cls.count))
    def __getitem__(self, indx):
        return self.weight[indx]
    # 객체에 대해서 [2] 기호가 있으면(print(f"현재체중은 {new_person[2]}"))), self.weight[indx]얘가 호출이 되고 인덱스가 self.weight로 넘어가서 출력을한다

    def __del__(self): # 소멸자, 언제호출이 되는가 ->
        print("객체 {}이 소멸됨".format(self.name))
        # 홍, 킴 소멸됨 , 프로그램이 종료되면 객체는 자동으로 반환 (자바에서 가비지 콜렉터) > 파이썬에도 있다 > 파이썬 컴파일러가 자동으로 수거함
        # 그럼 소멸자는 왜 만들어? 쓸일은 별로 없다네

#Person('guest', 11, 'jeju') # 객체가 만들어졌는데 변수가없어 > 붕떴어 > 가비지콜렉터행
    
    # def __call__(self):
    #     return self.weight / self.height * 2

    # def __len__(self):
    #     return len(self.weight)

    def __str__(self) -> str:
        pass

    def __str__(self): # Person은 객체인데 출력하려면 스트링이 필요해, 스트링을 만들어주는 함수를 정의할 수 있어
        return "{}\t{}\t{}".format(self.name, self.age, self.address)

    # def show_person_vision(self): # BMI하기전에 지움
    #     print("시력은 {}".format(self.__vision))# 여기는 뉴퍼슨이 아니라 셀프지 -> 왜? ->

    def __eq__(self, other):
        return self.age == other.age

new_person = Person('hong', 20, 'busan')
other_person = Person('Kim', 30, 'masan')
Person.printing()###클래스메소드 호출 / 클래스명.
new_person.printing()###객체라고해서 달라진건 없다. 같다
print(f"객체의 나이는**{new_person.age:5}***") # 다섯칸에 걸쳐서 찍으라는 말, *는 몇칸띄는지 잘보이라고 그냥 넣은 것
print("객체의 타입은 {}".format(isinstance(new_person, Person))) #왼쪽의 객체가 오른쪽의 클래스에 해당하는 객체냐는 함수 > 값 true
print("이 사람은 {}".format(new_person.name)) # false로 뜸 > 근데 otherperson 지역을 부산으로 바꾸면 true로 뜸 > 스트링도 그냥 떄려버리네 파이썬 코딩의 막강함

print(f"현재체중은 {new_person[2]}")

# print(f"체질량은 {new_person()}") ###__call__() 함수가 호출
print(new_person == other_person) # 자바에서 객체비교하던거

print(f"몸무게는 {new_person.weight}")
#print("시력은 {}".format(new_person.__vision))
new_person.show_person_vision()
print(str(new_person)) #str은 함수인데 뉴퍼슨은 객체잖아/이상하지않음?/다른애들은 변수.메소드인데/둘 다? 퍼슨의 메소드인데 위에거랑 호출하는 방식이 달라
# 그니까 new_person.str() 이렇게 써야할 것 같은데 > 해봐 > .을하면 함수이름이 나와야 됨
print(new_person.__str__()) # 오 이것도 된다.
print(str(new_person)) # 이게 내츄럴한 코딩이래 약간 자연어쪽에 가까운?
print(new_person) #뉴오브젝은 스트링이 아니잖아 > 자동변환해줌 > new_person만 했지만 .__str__()이 자동으로 호출되어온것

print(f"리스트 길이 {len(new_person)}") # 리스트길이 7 # 뉴퍼슨은 객체인데 렌을치면 위에 __렌__함수가 호출이 된다.

my_list = [1,2,3,4]
print(len(my_list))

print(f"{Person.count}객체가 생성됨")
print(f"{other_person.count}객체가 생성됨")
print(f"{new_person.count}객체가 생성됨")