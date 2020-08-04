T = int(input())
for tc in range(1, T + 1):
    s = []
    max_ = 0
    for i in range(5):
        s.append(list(input()))
        max_ = max(max_, len(s[-1]))
    for i in range(5):
        if len(s[i]) < max_:
            s[i].extend([''] * (max_ - len(s[i])))
    ans = ''
    for i in range(max_):
        for j in range(5):
            ans += s[j][i]
    print(f'#{tc} {ans}')