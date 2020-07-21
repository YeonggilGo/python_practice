T = int(input())

for tc in range(1, T + 1):
    print(
        f'#{tc} {sum([a for a in list(map(int,input().split())) if a%2 == 1])}')
