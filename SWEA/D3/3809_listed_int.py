# 완전 탐색으로 풀었는데 썩 맘에 들지는 않는다.

import math
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = []
    while len(num) < N:
        num.extend(list(map(int, input().split())))
    tmp = ''.join(map(str, num))
    i = 0
    while True:
        if str(i) in tmp:
            i += 1
            continue
        else:
            break

    print(f'#{tc} {i}')
