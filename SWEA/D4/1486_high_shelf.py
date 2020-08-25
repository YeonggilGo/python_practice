from itertools import combinations as coms

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    ans = sum(H)
    for i in range(1, N + 1):
        for com in coms(H, i):
            if B <= sum(com) < ans:
                ans = sum(com)
    print(f'#{tc} {ans - B}')

# 재귀로 하는게 더좋다. 최악의 경우에는 같지만 그렇지 않다면 이쪽이 빠르다.
# stack을 활용 할 수도 있다.

# def sol(h, i):
#     global a
#     if h >= b:
#         a = min(a, h)
#         return
#     if i > n - 1:
#         return
#     sol(h, i + 1);
#     sol(h + l[i], i + 1)
#
# for t in range(int(input())):
#     a = 1 << 32;
#     n, b = map(int, input().split());
#     l = list(map(int, input().split()));
#     sol(0, 0);
#     print(f'#{t + 1}', a - b)
