import re

f = open("Day 1/d1i.txt", "r")
lines = f.readlines()
#do I like regexes? absolutely not
#they're very fiddly
#but goddamnit they're efficient
#this section is to make the conversion really easy from string to number
string_dict = {"one": "1",  "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
num_dict = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
useful_dict = string_dict | num_dict
values = 0
for line in lines:
    num_list = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[123456789]))", line)
    num = int(useful_dict[num_list[0]]+useful_dict[num_list[-1]])
    values += num
print(values)