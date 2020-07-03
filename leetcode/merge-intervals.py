# Runtime: 80 ms, faster than 97.55% of Python3 online submissions for Merge Intervals.
# Memory Usage: 15.5 MB, less than 88.48% of Python3 online submissions for Merge Intervals.

def merge(intervals):
  if len(intervals) <= 1:
    return intervals
  # Interval denoted as [x,y]
  xs = []
  ys = []
  for interval in intervals:
    xs.append(interval[0])
    ys.append(interval[1])
  xs.sort()
  ys.sort()
  # Iteration index
  i = 1
  newIntervals = []
  # Stores the values of new interval to add
  x = xs[0]
  y = ys[0]
  # Iterate through lists
  while i < len(intervals):
    # If found overlap value, track potential corresponding y value
    if xs[i] <= ys[i-1]:
      y = ys[i]
      i += 1
    # If no overlap found, add interval
    else:
      newIntervals.append([x, y])
      y = ys[i]
      x = xs[i]
      i += 1
  # Add last interval of x,y values
  newIntervals.append([x,y])
  return newIntervals

      

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[0,4]]))
print(merge([[0,0],[1,4]]))
print(merge([[1,4],[0,0]]))
print(merge([[1,4],[0,2],[3,5]]))
