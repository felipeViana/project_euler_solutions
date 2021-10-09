MAX = 101

result = 0

for i in range(1, MAX):
  for j in range(1, MAX):
    if i != j:
      result += i * j

print(result)