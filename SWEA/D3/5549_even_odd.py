T = int(input())
for tc in range(1,T+1):
    N = int(input()[-1])
    ans = 'Odd' if N%2 else 'Even'
    print(f'#{tc} {ans}')