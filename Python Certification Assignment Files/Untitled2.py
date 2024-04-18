import re

file = open("bub.txt")

numlist = list()

count = 0

for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if not numbers: continue
    for num in numbers:
        new_num = int(num)
        count = count + new_num

    


print(count)