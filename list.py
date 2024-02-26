bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[3])
#print(bicycles[4])#일부러 에러내서 읽고 해결하는 연습
print(bicycles[-1])#-1은 항상 마지막요소 반환
print(bicycles[-2])#리스트의 길이를 알지 못할때 이런식으로 하면 매우 유용, -1이 마지막이니 -2은 마지막앞이지

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#practice
friends_name = ['철수', '영희', '영호', '경희']

#3.2.1 요소 수정
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'#바꿔지는 것 확인
print(motorcycles)
motorcycles[-1] = 'BMW'#바꿔지는 것 확인
print(motorcycles)

#3.2.2 요소 추가
motorcycles.append('GM')#어펜드 : 뒤에 추가하는 것 확인
#motorcycles.append('GM', 'KIA') #두개는 안되나봐
print(motorcycles)
motorcycles.insert(2,'AUDI')#3번째에 아우디 들어간 것 확인
print(motorcycles)

#3.2.3 요소 제거
del motorcycles[0]#del문은 .을 안쓰네
print(motorcycles)
del motorcycles[-1]#마지막에 들어간 GM 제거 확인
print(motorcycles)

motorcycles.pop(-2)
print(motorcycles)#뒤에서 두번째인 AUDI 제거 확인
motorcycles.pop()
print(motorcycles)#남은 것 중에 '마지막으로 추가된' 리스트 BMW 제거 확인
popped_motor = motorcycles.pop()
print(motorcycles)#82page복습
print(popped_motor)#82page복습
#83page도 해봐
#85p~86p 연습문제 따로 파일 만들어서 해봐

#3.3.1
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()#리스트 자체를 수정
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))#임시로 정렬, 실제 순서는 바뀌지 않음((cars)>파라미터 전달)
print(cars)#실제 순서는 바뀌지 않은 것 확인
#print(sorted(cars, resverse=True)) #이거는 왜 오류
print(len(cars))#length
print(cars[3])#length는 4지만 0123이기때문에 index4는 없고 마지막거가 index3임
