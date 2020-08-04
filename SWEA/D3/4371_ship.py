# 시간 초과

# from collections import deque
# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     funny_days = deque([])
#     for _ in range(N):
#         funny_days.append(int(input()))

#     funny_days.popleft()
#     cnt = 0
#     while funny_days:
#         ship = funny_days.popleft()
#         cnt += 1
#         period = ship - 1
#         while ship + period in funny_days:
#             funny_days.remove(ship + period)
#             ship += period

#     print(f'#{tc} {cnt}')

# 2차시도 : 시간 초과
# from collections import deque
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     funny_days = deque([])
#     for _ in range(N):
#         funny_days.append(int(input()))
#     funny_days.popleft()
#     check = [0] * len(funny_days)
# 
#     cnt = 0
#     for i in range(len(funny_days)):
#         ship = funny_days[i]
#         if check[i]:
#             continue
# 
#         cnt += 1
#         period = ship - 1
#         for j in range(ship, funny_days[-1]+1, period):
#             if j in funny_days:
#                 check[funny_days.index(j)] = 1
#     print(f'#{tc} {cnt}')

# 3차 시도

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ships = []
    a = int(input())
    for _ in range(N - 1):
        ships.append(int(input()) - 1)

    cnt_ships = []
    for ship in ships:
        check = True
        for cnt_ship in cnt_ships:
            if ship % cnt_ship == 0:
                check = False
                break
        if check:
            cnt_ships.append(ship)

    print(f'#{tc} {len(cnt_ships)}')
