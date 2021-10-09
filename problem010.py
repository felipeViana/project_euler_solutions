MAX = 2 * 1000 * 1000

primes = []
for i in range(0, MAX):
  primes.append(True)

primes[2] = True
for i in range(4, MAX, 2):
  primes[i] = False

for i in range(3, MAX, 2):
  if primes[i]:
    for j in range(i + i, MAX, i):
      primes[j] = False

primes[0] = False
primes[1] = False

sum = 0
for i in range(len(primes)):
  if primes[i] == True:
    sum += i

print(sum)