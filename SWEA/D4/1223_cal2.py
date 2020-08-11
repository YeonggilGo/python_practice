for tc in range(1, 11):
    N = int(input())
    exp = input()
    exp_list = exp.split('+')
    new_exp = ''
    for i in range(len(exp_list)):
        if '*' in exp_list[i]:
            tmp = exp_list[i].split('*')
            for each in tmp:
                if each != '*':
                    new_exp += each
            new_exp += '*+'
        else:
            if exp_list[i] == '+':
                continue
            new_exp += exp_list[i] + '+'
    new_exp = new_exp.split('+')
    ans = 0
    for i in range(len(new_exp)):
        if not new_exp[i]:
            continue
        if '*' in new_exp[i]:
            tmp = 1
            for each in new_exp[i]:
                if each == '*':
                    continue
                else:
                    tmp *= int(each)
            ans += tmp
        else:
            ans += int(new_exp[i])

    print(f'#{tc} {ans}')

