def info_car(manufacturer, model, **options):
    """자동차 정보 보여주는 함수"""
    dic_car = {
        'manufacturer': manufacturer.upper(),
        'model': model.title(),
        }
    for option, value in options.items():
        dic_car[option] = value

    return dic_car

inventory_morning = info_car('kia', 'morning', year = 2017, color = 'black', sun_roof = False)
print(inventory_morning)

inventory_k5 = info_car('kia', 'k5', year = 2023, color = 'white', sun_roof = True)
print(inventory_k5)