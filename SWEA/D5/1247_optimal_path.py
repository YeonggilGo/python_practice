def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dfs(pos, total):
    global answer
    if total >= answer:
        return
    if all(check):
        total += dist(e, pos)
        if total < answer:
            answer = total
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            dfs(places[i], total + dist(pos, places[i]))
            check[i] = 0


for tc in range(int(input())):
    N = int(input())
    temp = list(map(int, input().split()))
    s, e = temp[:2], temp[2:4]
    places = [temp[2 * i:2 * i + 2] for i in range(2, 2 + N)]
    answer = float('inf')
    check = [0 for _ in range(N)]
    dfs(s, 0)
    print('#{} {}'.format(tc + 1, answer))


# If I use permutation, program executes very slow than using dfs.
#
# from itertools import permutations as pers
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     temp = list(map(int, input().split()))
#     s, e = temp[:2], temp[2:4]
#     places = [temp[2 * i:2 * i + 2] for i in range(2, 2 + N)]
#     answer = float('inf')
#     for per in pers(places):
#         flag = 0
#         total = dist(s, per[0]) + dist(per[-1], e)
#         for i in range(1, N):
#             total += dist(per[i], per[i - 1])
#             if total > answer:
#                 flag = 1
#                 break
#         if not flag:
#             answer = total
#     print('#{} {}'.format(tc + 1, answer))
