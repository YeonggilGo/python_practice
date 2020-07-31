T = int(input())

for tc in range(1, T + 1):
    s = input()
    ans = ''
    for l in s:
        if l not in 'aeiou':
            ans += l
    print(f'#{tc} {ans}')