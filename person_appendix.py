class Shape:
    def __init__(self, base, height):
        self.__base = base # 언더라인치면 프라이빗 변수
        self.__height = height

    @property # decorator for getter // getter는 필드값이 있는애를 얘기하는거고
    def get_base(self): # get_height는 읽기만 하는 함수다
        return self.__base # base를 return

    def get_height(self): # get_height는 읽기만 하는 함수다
        return self.height
    
    @height.setter
    def height(self, value):
        self.__height = value

def get_data():
    return 1,2,3

_,a,b = get_data() # 겟데이터가 세개를 리턴하는데 맨앞에거는 무시할거야 : _

a = [1,2,3]
b = [11,22,33]
mylist = [*a,*b] # '*' -> 여러개하라는 의미 >> 병합
print(mylist)
c = ['a','b']
z = zip(a,c)
#print(z) > # 이렇게하면 객체를 출력이라서 오류
print(list(z)) # a는 3개고 c는 2개잖아 >> 2개만 >> zipper연상
### getter, setter를 정의하는데 decorator(자바에서의 annotation) ###
