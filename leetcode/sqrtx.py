# Runtime: 20 ms, faster than 99.57% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Sqrt(x).

import math

def mySqrt(x: int) -> int:
  return math.floor(math.sqrt(x))

print(mySqrt(4))
print(mySqrt(8))