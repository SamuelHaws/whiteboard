# Certainly not the most optimal solution out there, 
# but sometimes the Leetcode "hard" problems tend to work out that way.
# I'm not a huge fan of this problem since it counts single points as lines...

# Runtime: 684 ms, faster than 12.56% of Python3 online submissions for Max Points on a Line.
# Memory Usage: 15.3 MB, less than 22.90% of Python3 online submissions for Max Points on a Line.

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
def maxPoints(points):
  if (len(points)) < 2:
    return len(points)

  # Store number of occurrences of each point in points
  # String representation of point as key (lists are not hashable), count as value
  points_counts = {str(point) : points.count(point) for point in points}

  # Initial highest number of points on any line is the highest count of a single point 
  # Consider input [[0,0],[0,0],[0,0]], where no lines will be calculated
  max_val = max(points_counts.values())

  # Copy points to new list with no duplicates
  points_distinct = []
  [points_distinct.append(pt) for pt in points if pt not in points_distinct]

  # Generate lines
  # Each line is a tuple: (isVertical, line function, any extra parameters...)
  lines = [] 
  # Point 1
  i = 0
  while i < len(points_distinct) - 1:
    j = i + 1
    # Point 2
    while j < len(points_distinct):
      # Calculate change in x and y, determines if line is vertical
      dx = points_distinct[j][0] - points_distinct[i][0]
      dy = points_distinct[j][1] - points_distinct[i][1]
      # If vertical, add x value (location of vertical line) to lines
      if (dx == 0):
        x_val = points_distinct[i][0] # points_distinct[j][0] would also work
        lines.append((True, x_val))
      # Otherwise use point-slope to get line function and add to lines (with current point values)
      # Point values are not accessed until line_function is called, so we have to store the current iteration
      else:
        point_slope_x1 = points_distinct[i][0]
        point_slope_y1 = points_distinct[i][1]
        def line_function(x, x1, y1, dx_arg, dy_arg):
          return y1 + dy_arg * (x - x1) / dx_arg
        lines.append((False, line_function, point_slope_x1, point_slope_y1, dx, dy))
      j += 1
    i += 1
  
  # Count number of points on each line, track highest value
  for line in lines:
    points_on_line = 0
    for point in points_distinct:
      # If vertical line
      if line[0]:
        # If point found on line
        if line[1] == point[0]:
          points_on_line += points_counts[str(point)]
      else:
        # If point found on line
        if line[1](point[0], line[2], line[3], line[4], line[5]) == point[1]:
          points_on_line += points_counts[str(point)]
    if points_on_line > max_val:
      max_val = points_on_line

  return max_val





# Test cases

print(maxPoints([[1,1],[1,2],[2,2],[3,2]]), ' ...expected: 3')
print(maxPoints([[1,1],[1,1],[2,2],[2,2]]), ' ...expected: 4')
print(maxPoints([[1,1],[1,1],[3,3],[5,5]]), ' ...expected: 4')
print(maxPoints([[1,1],[3,3],[3,3],[5,5]]), ' ...expected: 4')
print(maxPoints([[1,1],[3,3],[5,5],[5,5]]), ' ...expected: 4')
print(maxPoints([]), ' ...expected: 0')
print(maxPoints([[0,0]]), ' ...expected: 1')
print(maxPoints([[0,0],[0,0]]), ' ...expected: 2')
print(maxPoints([[0,0],[0,0],[0,0]]), ' ...expected: 3')
print(maxPoints([[1,1],[2,2],[3,3]]), ' ...expected: 3')
print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]), ' ...expected: 4')
print(maxPoints([[0,0],[1,1],[0,0]]), ' ...expected: 3')
print(maxPoints([[0,0],[0,1],[0,2]]), ' ...expected: 3')
print(maxPoints([[4,0],[4,-1],[4,5]]), ' ...expected: 3')
print(maxPoints([[1,1],[1,1],[2,2],[2,2]]), ' ...expected: 4')
print(maxPoints([[0,0],[94911150,94911151],[94911151,94911152]]), ' ...expected: 2')