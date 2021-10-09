import math

def largest_prime(number):

  while number % 2 == 0:
    print(2)
    number = number / 2

  for i in range(3, int(math.sqrt(number)) + 1, 2):
    while number % i == 0:
      print(i)
      number = number / i

  return 0



# print(largest_prime(13195))
print(largest_prime(600851475143))