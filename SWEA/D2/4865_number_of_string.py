T = int(input())
for tc in range(1, T + 1):
    tar = set(input())
    given = input()
    tar_dict = {key: 0 for key in tar}
    for letter in given:
        if letter in tar_dict:
            tar_dict[letter] += 1
    ans = max(tar_dict.values())
    print('#{} {}'.format(tc, ans))
