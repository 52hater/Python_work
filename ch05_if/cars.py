cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw' or car == 'audi':
        print(car.upper())
    else:
        print(car.title())