# used in problem 11

def reverse_rows(matrix):
  new_matrix = []
  for row in matrix:
    new_row = row.copy()
    new_row.reverse()
    new_matrix.append(new_row)

  return new_matrix

def transpose(matrix):
  new_matrix = []

  for column in range(0, len(matrix[0])):
    new_row = []
    for row in matrix:
      new_row.append(row[column])
    new_matrix.append(new_row)

  return new_matrix

# adds 1 to rows, to easily calculate diagonal products
def shift(matrix):
  new_matrix = []
  for i in range(0, len(matrix)):
    # add 1's before
    new_row = []
    for j in range(0, i):
      new_row.append(1)

    # add row
    for j in matrix[i]:
      new_row.append(j)

    # add 1's after
    for j in range(i + 1, len(matrix)):
      new_row.append(1)

    new_matrix.append(new_row)

  return new_matrix

