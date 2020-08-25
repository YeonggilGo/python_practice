# find index from end to the start
def find_reverse(li, tar):
    for i in range(len(li) - 2, -1, -1):
        if li[i] == tar:
            return i
    return len(li) - 1


T = int(input())
for tc in range(1, T + 1):
    p = input()
    t = input()
    # pi : distance which move if list has same letter
    pi = list(range(len(p) - 1, 0, -1)) + [len(p)]
    idx = len(p) - 1
    while idx < len(t):
        find = 1
        for i in range(len(p)):
            if p[len(p) - 1 - i] != t[idx - i]:
                find = 0
                break

        if find:
            break
        else:
            # Boyer Moore algorithm :
            # 1. if last letter of p is same with t[idx]
            # -> if t have same letter in another position : move distance of another one
            # else : move len(t)
            # 2. elif (last letter is diffenrent with t[idx]
            # -> move distance pi[t[idx]]
            # 3. else -> move len(p)
            if t[idx] in p:
                idx += pi[find_reverse(p, t[idx])]
            else:
                idx += len(p)
    print(f'#{tc} {find}')
