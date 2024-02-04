def find_the_num(numbers):
  hashMap = {}
  for num in numbers:
    if num not in hashMap:
      hashMap[num] = 1
    else:
      hashMap[num] += 1

  maxNum = 0
  for key in hashMap:
    if hashMap.get(key) == key and key > maxNum:
      maxNum = key

  return maxNum
