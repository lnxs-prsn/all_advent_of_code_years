# part 1

# with open('chilling/aoc2_input.txt', 'r', encoding='utf-8') as ff:
#     lines = ff.readlines()

# total = 0
# for num in lines:
#     alist = num.split('x')
#     alist = [int(x) for x in alist]
#     l,w,h = alist
#     smallest = min(l*w,w*h, h*l)
#     total += (2*l*w + 2*w*h + 2*h*l + smallest)


# print(total)

#part 2

with open('chilling/aoc2_input.txt', 'r', encoding='utf-8') as ff:
    lines = ff.readlines()
# lines = ['2x3x4','1x1x10']
total = 0
for num in lines:
    alist = num.split('x')
    alist = [int(x) for x in alist]
    l,w,h = alist
    s1 = min(alist)
    s2 =  sum(alist) - s1 - max(alist)
    ribbon = s1+s1+s2+s2
    bow = l*w*h
    total += (bow+ribbon)


print(total)