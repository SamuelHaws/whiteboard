# Runtime: 28 ms, faster than 98.85% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.6 MB, less than 94.25% of Python3 online submissions for Kids With the Greatest Number of Candies.

def kidsWithCandies(candies, extraCandies):
  maxCandy = max(candies)
  for i, e in enumerate(candies):
    if candies[i] + extraCandies < maxCandy:
      candies[i] = False
    else:
      candies[i] = True
  return candies

print(kidsWithCandies([2,3,5,1,3], 3))