SUM = 1000

for a in range(1, SUM):
  for b in range(a + 1, SUM):
    c = SUM - a - b
    if a * a  + b * b == c * c:
      print(a, b, c, a * b * c)