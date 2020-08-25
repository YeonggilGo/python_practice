import math


def solve(n):
    if n in can_enter:
        return can_enter[n]

    can_enter[n] = made_by_calculator(n)
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            a = solve(i)
            b = solve(n // i)
            # If you can't enter either number
            if a == 99999 or b == 99999:
                tmp = 99999
            else:
                tmp = a + b + 1

            can_enter[n] = min(tmp, can_enter[n])
    return can_enter[n]


def made_by_calculator(n):
    cnt = 0
    while n > 0:
        tmp = n % 10
        if tmp not in can_use:
            return 99999
        n //= 10
        cnt += 1
    return cnt


if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        tmp = input().split()
        # can_use : numbers that can use in calculator
        can_use = [i for i in range(len(tmp)) if tmp[i] == '1']
        tar = int(input())
        # can_enter (dict) ->  key : numbers that can enter by broken calculator,
        #                      val : number of times that calculator is pressed to enter the number
        can_enter = {key: 1 for key in can_use}
        solve(tar)
        if can_enter[tar]:
            ans = can_enter[tar] + 1
        else:
            ans = -1
        print(f'#{tc} {ans}')
