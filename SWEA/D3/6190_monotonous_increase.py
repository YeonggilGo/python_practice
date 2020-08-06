from itertools import combinations as combs


def is_mono(n):
    n = str(n)
    for i in range(1, len(n)):
        if n[i] < n[i - 1]:
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for comb in combs(A, 2):
        num = comb[0] * comb[1]
        if is_mono(num):
            if ans < num:
                ans = num
    if ans == 0:
        ans = -1
    print(f'#{tc} {ans}')