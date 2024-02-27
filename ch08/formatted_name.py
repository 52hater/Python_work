def get_formatted_name(first_name, last_name, middle_name = ''):
    """실제 이름을 깔끔한 형식으로 반환합니다."""
    if middle_name: #미들네임이 빈 스트링이면 FALSE로 간주
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title() # 리턴의 타입 스트링인데 지정안해 파이썬 컴파일러가 알아서 함

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)