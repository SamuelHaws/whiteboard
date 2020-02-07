"""
Runtime: 20 ms, faster than 97.86% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
"""

def isValid(s: str) -> bool:
  if len(s) == 0:
    return True
  if len(s) == 1:
    return False
  parensOpen = 0
  squaresOpen = 0
  curlysOpen = 0
  opens = []
  try:
    for c in s: 
      if c == '(':
        parensOpen += 1
        opens.append('(')
      elif c == '[':
        squaresOpen += 1
        opens.append('[')
      elif c == '{':
        curlysOpen += 1
        opens.append('{')
      elif c == ')':
        if not opens[len(opens)-1] == '(':
          return False
        parensOpen -= 1
        opens.pop()
      elif c == ']':
        if not opens[len(opens)-1] == '[':
          return False
        squaresOpen -= 1
        opens.pop()
      elif c == '}':
        if not opens[len(opens)-1] == '{':
          return False
        curlysOpen -= 1
        opens.pop()
  except IndexError: # occurs when there are more closing brackets than open
    return False

  if parensOpen > 0 or squaresOpen > 0 or curlysOpen > 0:
    return False

  return True

print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([)]"))      # False
print(isValid("{[]}"))      # True
print(isValid("[{()}]"))    # True