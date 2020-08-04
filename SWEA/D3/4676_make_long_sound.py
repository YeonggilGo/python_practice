T = int(input())

for tc in range(1, T + 1):
    s = input()
    H = int(input())
    pos = list(map(int, input().split()))
    cnt_pos = [0] * (len(s) + 1)

    for each in pos:
        cnt_pos[each] += 1

    new_s = ''
    for i in range(len(s) + 1):
        if cnt_pos[i]:
            new_s += '-' * cnt_pos[i]
        if i != len(s):
            new_s += s[i]

    print(f'#{tc} {new_s}')