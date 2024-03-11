a, b = input().split()
a, b = int(a), int(b)
if(a > b): # 괄호 없어도됨
    print('>')
elif(a < b):
    print('<')
else:
    print('==')
