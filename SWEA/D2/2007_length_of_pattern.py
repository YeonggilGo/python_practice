T = int(input())

for tc in range(1, T + 1):
    s = input()
    tmp = ''
    ans = []
    for i in range(len(s)):
        tmp += s[i]
        if s[len(tmp): len(tmp) * 2] == tmp:
            ans.append(tmp)
            break
    print(f'#{tc} {len(ans[0])}')
