a = 1
b = 1

index = 2

while b < 10**999:
  aux = b
  b = a + b
  a = aux
  index += 1


print(b, index)
