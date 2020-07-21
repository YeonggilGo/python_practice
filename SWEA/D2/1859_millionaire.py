from collections import deque
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    money = 0
    largest = price[-1]

    for i in range(N - 1, -1, -1):
        if largest < price[i]:
            largest = price[i]
        else:
            money += largest - price[i]

    print(f'#{tc} {money}')
