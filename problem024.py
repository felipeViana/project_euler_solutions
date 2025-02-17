current = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = 1

goal = 1000000

def next_permutation(arr):
  n = len(arr)

  # find pivot
  pivot = -1
  for i in range(n - 2, -1, -1):
    if arr[i] < arr[i+1]:
      pivot = i
      break

  # if no pivot, reverse whole array
  if pivot == -1:
    arr.reverse()
    return

  # find element from right that is greater than pivot
  for i in range(n - 1, pivot, -1):
    if (arr[i] > arr[pivot]):
      arr[i], arr[pivot] = arr[pivot], arr[i]
      break

  # reverse elements from pivot + 1 to end
  left, right = pivot + 1, n - 1
  while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

  return arr



while permutations < goal:
  current = next_permutation(current)
  permutations += 1


print(''.join(str(x) for x in current))
