from collections import deque
T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    cus = deque(sorted(list(map(int, input().split()))))
    bread = 0
    sell = 0

    can_sell = True
    while cus:
        tar = cus.popleft()
        bread = (tar//M)*K
        sell += 1
        if sell > bread:
            can_sell = False
            break

    ans = 'Possible' if can_sell else 'Impossible'
    print(f'#{tc} {ans}')
