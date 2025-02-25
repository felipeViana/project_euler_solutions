# If the numbers to are written out in words: one, two, three, four, five, then there are 19

# letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example,
# 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def number_to_str(number):
  if number == 1000:
    return "onethousand"

  if number > 99:
    t = 0
    while number > 99:
      number -= 100
      t += 1

    if number > 0:
      return number_to_str(t) + "hundredand" + number_to_str(number)
    else:
      return number_to_str(t) + "hundred"

  if number >= 90:
    return "ninety" + number_to_str(number - 90)
  if number >= 80:
    return "eighty" + number_to_str(number - 80)
  if number >= 70:
    return "seventy" + number_to_str(number - 70)
  if number >= 60:
    return "sixty" + number_to_str(number - 60)
  if number >= 50:
    return "fifty" + number_to_str(number - 50)
  if number >= 40:
    return "forty" + number_to_str(number - 40)
  if number >= 30:
    return "thirty" + number_to_str(number - 30)
  if number >= 20:
    return "twenty" + number_to_str(number - 20)

  if number == 0:
    return ""

  if number == 1:
    return "one"
  if number == 2:
    return "two"
  if number == 3:
    return "three"
  if number == 4:
    return "four"
  if number == 5:
    return "five"
  if number == 6:
    return "six"
  if number == 7:
    return "seven"
  if number == 8:
    return "eight"
  if number == 9:
    return "nine"

  if number == 10:
    return "ten"
  if number == 11:
    return "eleven"
  if number == 12:
    return "twelve"
  if number == 13:
    return "thirteen"
  if number == 14:
    return "fourteen"
  if number == 15:
    return "fifteen"
  if number == 16:
    return "sixteen"
  if number == 17:
    return "seventeen"
  if number == 18:
    return "eighteen"
  if number == 19:
    return "nineteen"

total = 0
for n in range(1, 1001):
  print(n, number_to_str(n), len(number_to_str(n)))
  total += len(number_to_str(n))

print(total)
