# Runtime: 48 ms, faster than 96.33% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 13.9 MB, less than 60.02% of Python3 online submissions for ZigZag Conversion.

def convert(s: str, numRows: int) -> str:
  if len(s) <= 1 or numRows <= 1:
    return s
  # Ex: for s = "PAYPALISHIRING", numRows = 3: rows[0] = "PAHN", rows[1] = "APLSIIG", etc.
  rows = [''] * numRows
  verticalColModOperand = numRows - 1
  # Track current row and column
  row = 0
  col = 0
  i = 0
  while (i < len(s)):
    # If on a vertical column
    if col % verticalColModOperand == 0:
      for j in range(numRows):
        if i >= len(s):
          break
        rows[j] += s[i]
        row += 1
        i += 1
      col += 1
      row -= 2
    # Else add to diagonal
    else:
      rows[row] += s[i]
      col += 1
      row -= 1
      i += 1
  ans = ''
  for row in rows:
    ans += row
  return ans




# print(convert("PAYPALISHIRING", 3))
# print(convert("PAYPALISHIRING", 4))