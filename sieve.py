# used in problems 7, 10, 12

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

print(primes)