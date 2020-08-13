import os

file_input = open("C:/Users/aclass/Desktop/python_practice/README.md", 'r', encoding='cp949')
# file_input = open("/Users/yeonggilgo/Documents/GitHub/python_practice/README.md", 'r', encoding = 'cp949')
input_data = file_input.readlines()

algo = {}
solved = {}
data = ''

for line in input_data:
    if line[0] == '|':
        break
    elif line == '\n':
        if pre == '\n':
            data += '\n'
    else:
        data += line + '\n'
    pre = line

for line in input_data:
    if line[0] == '|':
        if line.strip()[2].isdigit():
            tmp = line.strip('|').split('|')
            algo[tmp[0].strip()] = tmp[2].strip()
            solved[tmp[0].strip()] = tmp[3].strip()

cnt = 0
bl = ''

for i in range(1, 5):
    # os.chdir(r'/Users/yeonggilgo/Documents/GitHub/python_practice/SWEA/D' + str(i))
    os.chdir(r'C:/Users/aclass/Desktop/python_practice/SWEA/D'+str(i))
    filenames = os.listdir('.')
    filenames.sort()
    num = []
    title = []
    for filename in filenames:
        num.append(filename[:4])
        title.append(filename[4:])
    if i == 1:
        data += f'''| Number | Title        | Algorithm |try again|\n| ------ | ------------ | --------- |---------|\n'''
    else:
        data += f'''\n\n### D{i}\n\n
| Number | Title        | Algorithm |try again|\n| ------ | ------------ | --------- |---------|\n'''

    for j in range(len(num)):
        al = algo[num[j]] if num[j] in algo else bl
        so = solved[num[j]] if num[j] in solved else bl
        data += f'''|{num[j]}|{title[j][1:-3]}|{al}|{so}|\n'''
        cnt += 1


file_output = open("C:/Users/aclass/Desktop/python_practice/README.md", 'w')
# file_output = open("/Users/yeonggilgo/Documents/GitHub/python_practice/README.md", 'w')

file_output.write(data)

file_input.close()
file_output.close()
