import math


num = 2 ** 1000

n = str(num)

sum = 0

for digit in n:
  sum = sum + int(digit)

print sum