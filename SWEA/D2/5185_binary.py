for tc in range(1, int(input()) + 1):
    N, h = input().split()
    ans = bin(int(h,16))[2:]
    ans = '0' * (int(N)*4 - len(ans)) + ans
    print('#{} {}'.format(tc, ans))