from decimal import *

getcontext().prec = 10000

def find_pattern_size(number):

  n_str = str(number)

  size = len(n_str)

  if size < 500:
    return 0

  # try pattern of each size k
  for k in range(1, (size - 2) // 2 + 1, 1):

    subset = n_str[2:2 + k]

    found = True
    for i in range(2 + k, size - k + 1, k):
      new_subset = n_str[i : i + k]
      if new_subset != subset:
        found = False
        break

    if found:
      return k

  # try with delayed start
  return find_pattern_size(n_str[0:2]+n_str[3:])



largest_recurr = 0
largest_number = 0

for i in range(2, 1000, 1):
  number = Decimal(1)/Decimal(i)
  # print("i = ", i)
  # print("going to find pattern for ", number)

  x = find_pattern_size(number)

  # print(x, "\n")

  if x > largest_recurr:
    largest_recurr = x
    largest_number = i

print(largest_number, largest_recurr)
