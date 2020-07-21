import datetime

T = int(input())

for tc in range(1, T + 1):
    m1, d1, m2, d2 = list(map(int, input().split()))

    print(f'#{tc} {(datetime.datetime(1,m2,d2)-datetime.datetime(1,m1,d1)).days+1}')
