import sys


def binary_search(l, r, tar, cnt):
    c = int((l + r) / 2)
    cnt += 1
    if c == tar:
        return cnt
    elif c > tar:
        return binary_search(l, c, tar, cnt)
    else:
        return binary_search(c, r, tar, cnt)


sys.stdin = open('이진탐색.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    cnt_A = binary_search(1, P, Pa, 0)
    cnt_B = binary_search(1, P, Pb, 0)
    if cnt_A < cnt_B:
        ans = 'A'
    elif cnt_A == cnt_B:
        ans = '0'
    else:
        ans = 'B'
    print('#{} {}'.format(tc,ans))
