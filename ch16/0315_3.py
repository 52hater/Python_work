# 460~

# with open('c.csv') as f: # c.csv가 없으니 에러가 나겠지 / No such file or directory: 'c.csv'
#     for line in f:
#         print(line)

# 이걸 익셉션 처리하려면? 트라이캐치

try:        
    with open('c.csv', 'r') as f: # c.csv가 없으니 에러가 나겠지 / No such file or directory: 'c.csv'
        for line in f:
            print(line)
except Exception as e:
        pass
        #print(e)

# 하지만 이렇게 짜면 절대 안되지ㅋㅋ