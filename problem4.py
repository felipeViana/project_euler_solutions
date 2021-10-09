def is_palindrome(number):
  s = str(number)

  return s == s[::-1]

greatest = 0
for i in range(900, 1000):
  for j in range(i + 1, 1000):
    if is_palindrome(i * j):
      greatest = max(greatest, i * j)

      print(i * j)

print(greatest)