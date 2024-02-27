def describe_pet(pet_name, animal_type = 'dog'): # 디폴트 파라미터(값을 전달하지 않으면 난 이걸 쓰겠다)
    """반려동물 정보를 표시합니다"""
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name}.") # 안에 어포스트로피가 있어서 바깥엔 ""

describe_pet('해리') # 여기서 애니멀타입없어 -> 디폴트 파라미터로 dog로 설정됨
describe_pet(pet_name = '해리')
describe_pet(pet_name='해리', animal_type='hamster')