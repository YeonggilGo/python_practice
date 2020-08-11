for tc in range(1, 11):
    N = int(input())
    exp = input()
    new_exp = exp[0]
    for i in range(1, len(exp), 2):
        new_exp += exp[i + 1] + exp[i]
    ans = int(new_exp[0])
    for i in range(1,len(exp),2):
        ans += int(new_exp[i])
    print(f'#{tc} {ans}')