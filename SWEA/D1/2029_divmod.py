import math
T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{tc} {divmod(a,b)[0]} {divmod(a,b)[1]}')
