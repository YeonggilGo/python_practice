for tc in range(1, 11):
    N, pwd = input().split()
    done = False

    while not done:
        done = True
        for i in range(len(pwd)-1):
            if pwd[i] == pwd[i + 1]:
                pwd = pwd[:i] + pwd[i + 2:]
                done = False
                break

    print(f'#{tc} {pwd}')
