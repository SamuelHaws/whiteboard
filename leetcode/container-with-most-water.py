# Runtime: 124 ms, faster than 91.30% of Python3 online submissions for Container With Most Water.
# Memory Usage: 15.3 MB, less than 74.87% of Python3 online submissions for Container With Most Water.

# Two pointer solution
def maxArea(height):
  maxSize = 0
  i = 0
  j = len(height) - 1
  while i < j:
    size = min(height[i], height[j]) * (j - i)
    if size > maxSize:
      maxSize = size
    if height[i] < height[j]:
      i += 1
    else:
      j -= 1
  return maxSize


print(maxArea([1,8,6,2,5,4,8,3,7]))