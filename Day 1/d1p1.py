import re
f = open("Day 1/d1i.txt", "r")
lines = f.readlines()
numbers = "[123456789]"
values = 0
for line in lines:
    num_list = re.findall(numbers, line)
    num = int(num_list[0]+num_list[-1])
    values += num
print(values)