with open('./aoc15_1input.txt', 'r', encoding='utf-8') as ff:
    line = ff.readline()

floora= 0
for index, x in enumerate(line):
    if x == '(':
        floora += 1
    if x == ')':
        floora -= 1

    if floora == -1:
        print(index+1)
        break