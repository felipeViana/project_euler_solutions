MAX = 2 * 1000 * 1000

prime_indices = []
for i in range(0, MAX):
  prime_indices.append(True)

prime_indices[2] = True
for i in range(4, MAX, 2):
  prime_indices[i] = False

for i in range(3, MAX, 2):
  if prime_indices[i]:
    for j in range(i + i, MAX, i):
      prime_indices[j] = False

prime_indices[0] = False
prime_indices[1] = False

primes = []
for i in range(len(prime_indices)):
  if prime_indices[i] == True:
    primes.append(i)

def count_factors(number):
  exponents = []

  prime_index = 0
  while number > 1:
    count = 0
    while number % primes[prime_index] == 0:
      number = int(number / primes[prime_index])
      count += 1

    exponents.append(count)
    prime_index += 1

  result = 1
  for i in exponents:
    result *= i + 1

  return result

triangular = 1
next = 2

while(count_factors(triangular) < 501):
  triangular += next
  next += 1

print(triangular)