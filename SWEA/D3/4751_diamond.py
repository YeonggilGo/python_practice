T = int(input())
for tc in range(1, T + 1):
    s = input()
    new_s = []
    for i in range(5):
        if i == 0 or i == 4:
            new_s.append('..' + '#...' * (len(s) - 1) + '#..')
        elif i == 1 or i == 3:
            new_s.append('.' + '#.'*(2*len(s)))
        else:
            tmp = ''
            for letter in s:
                tmp += f'#.{letter}.'
            tmp += '#'
            new_s.append(tmp)
    for line in new_s:
        print(line)
