fib0 = 1
fib1 = 2

MAX = 4 * 1000 * 1000
sum = 0

while(fib1 <= MAX):
  if fib1 % 2 == 0:
    sum += fib1

  aux = fib1
  fib1 = fib0 + fib1
  fib0 = aux

print(sum)