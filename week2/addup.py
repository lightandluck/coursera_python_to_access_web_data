import re

f = open('regex_sum_357521.txt')
data = f.read()

numbers = re.findall('[0-9]+', data)
count = 0
for row in numbers:
  count += int(row)

print(len(numbers))
print(count)

