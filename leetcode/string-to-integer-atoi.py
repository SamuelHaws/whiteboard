# Runtime: 28 ms, faster than 93.19% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 13.6 MB, less than 97.94% of Python3 online submissions for String to Integer (atoi).

# ASCII to integer
def myAtoi(s: str) -> int:
  num = ''
  isAcceptableLeadingChar = True
  for c in s:
    # Iterate through whitespace
    if isAcceptableLeadingChar and c == ' ':
      continue
    # Add sign if present
    if isAcceptableLeadingChar and (c == '+' or c == '-'):
      num += c
      isAcceptableLeadingChar = False
      continue
    if not c.isdigit():
      break
    isAcceptableLeadingChar = False
    num += c
  
  # If no valid conversion could be performed
  if num == '' or num == '+' or num == '-':
    return 0
  # Check for 32-bit signed integer overflow
  num = int(num)
  if(abs(num) > (2 ** 31 - 1)):
    if num < -(2 ** 31 - 1):
      return -2147483648
    else:
      return 2147483647
  return num

print(myAtoi("42"))
print(myAtoi("    -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))
print(myAtoi("+"))