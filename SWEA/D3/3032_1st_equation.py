T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())
    aa = [1, 0]
    bb = [0, 1]
    result = [0, 0, 0]
    while True:
        q = a // b
        a = a % b
        aa[0] = aa[0] - q*aa[1]
        bb[0] = bb[0] - q*bb[1]
        if a == 0:
            result[0] = b
            result[1] = aa[1]
            result[2] = bb[1]
            break
        q = b // a
        b = b % a
        aa[1] = aa[1] - q*aa[0]
        bb[1] = bb[1] - q*bb[0]
        if b == 0:
            result[0] = a
            result[1] = aa[0]
            result[2] = bb[0]
            break
    print(f'#{tc} {result[1]} {result[2]}')
