primes = [2]

MAX = 21

for i in range(3, MAX, 2):
  is_prime = True
  for j in primes:
    if i % j == 0:
      is_prime = False
  if is_prime:
    primes.append(i)

smallest_multiple = 1
for p in primes:
  factor = p
  while factor < MAX:
    factor = factor * p
  smallest_multiple = smallest_multiple * int(factor / p)




print(primes)
print(smallest_multiple)