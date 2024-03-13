# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

n = int(input())
if 1 <= n <= 10000:
    result = sum(range(1, n+1)) # n+1을 하는 이유는 range함수는 끝 값은 포함하지 않기 때문
    print(result)
else:
    print()