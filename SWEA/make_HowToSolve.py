import os

#file_input = open("C:/Users/GoYeongGil/Desktop/python_practice/SWEA/HowToSolve.md", 'r', encoding='UTF-8')
file_input = open(
    "/Users/mac/Documents/GitHub/python_practice/SWEA/HowToSolve.md", 'r', encoding='UTF-8')
input_data = file_input.readlines()

algo = {}
solved = {}

for line in input_data:
    if len(line.strip()) > 1:
        if line.strip()[2].isdigit():
            tmp = line.strip('|').split('|')
            algo[tmp[0].strip()] = tmp[2].strip()
            solved[tmp[0].strip()] = tmp[3].strip()

cnt = 0
bl = ''
data = '''# How To Solve'''

for i in range(1, 4):
    os.chdir(r'/Users/mac/Documents/GitHub/python_practice/SWEA/D'+str(i))
    filenames = os.listdir('.')
    filenames.sort()
    num = []
    title = []
    for filename in filenames:
        num.append(filename[:4])
        title.append(filename[4:])

    data += f'''\n\n### D{i}\n\n
| Number | Title        | Algorithm |try again|\n| ------ | ------------ | --------- |---------|\n'''
    for j in range(len(num)):
        al = algo[num[j]] if num[j] in algo else bl
        so = solved[num[j]] if num[j] in solved else bl
        data += f'''|{num[j]}|{title[j][1:-3]}|{al}|{so}|\n'''
        cnt += 1


#file_output = open("C:/Users/GoYeongGil/Desktop/python_practice/SWEA/HowToSolve.md", 'w')
file_output = open(
    "/Users/mac/Documents/GitHub/python_practice/SWEA/HowToSolve.md", 'w')


file_output.write(data)

file_input.close()
file_output.close()
