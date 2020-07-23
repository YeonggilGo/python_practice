for _ in range(10):
    t = int(input())

    tar = input()
    s = input()
    tar_rev = tar[::-1]

    pos = len(tar) - 1
    ans = 0
    while pos < len(s):
        if s[pos - len(tar) + 1:pos + 1] == tar:
            ans += 1
            pos += len(tar)
        else:
            if s[pos] in tar:
                tmp = tar_rev.index(s[pos])
                pos += tmp if tmp else len(tar)
            else:
                pos += len(tar)
    print(f'#{t} {ans}')
