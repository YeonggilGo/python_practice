T = int(input())

for tc in range(1, T + 1):
    num = list(map(int, input().split()))
    num.sort()
    print(f'#{tc} {round(sum(num[1:-1])/(len(num)-2))}')
