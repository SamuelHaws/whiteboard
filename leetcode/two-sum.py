# Runtime: 44 ms, faster than 96.41% of Python3 online submissions for Two Sum.
# Memory Usage: 14 MB, less than 65.81% of Python3 online submissions for Two Sum.
def twoSum(nums, target):
  myDict = {}
  for i, num in enumerate(nums):
    offset = target - num
    if offset not in myDict:
      myDict[num] = i
    else:
      print([myDict[offset], i])
      return [myDict[offset], i]

exNums = [2,7,11,3]
exTarget = 9

twoSum(exNums, exTarget)