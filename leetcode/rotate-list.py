# Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Rotate List.
# Memory Usage: 13.6 MB, less than 98.71% of Python3 online submissions for Rotate List.

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def printLN(ln):
  s = ''
  while (ln is not None):
    s += str(ln.val) + ','
    ln = ln.next
  print(s)

def rotateRight(head: ListNode, k: int) -> ListNode:
  # If linkedlist length is 0 or 1
  if head is None or head.next is None:
    return head
  # Iterate to end of list, counting nodes
  p = head
  numNodes = 1
  while p.next is not None:
    p = p.next
    numNodes += 1
  # Don't waste time doing extra work on a "360" rotation
  if numNodes == k:
    return head
  # Reduce k
  k = k % numNodes
  # Make cycle
  p.next = head
  # Determine amount of times to move head to the right
  rotateNum = 0
  if numNodes > k:
    rotateNum = numNodes - k
  else:
    if (numNodes % 2 == 0):
      rotateNum = numNodes + k
    else:
      rotateNum = numNodes + k + 1
  # Move head, assign tail
  i = 0
  p = head
  tail = None
  while (i < rotateNum):
    tail = p
    p = p.next
    i += 1
  head = p
  tail.next = None
  return head

head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
printLN(head)
printLN(rotateRight(head, 2))
print('-----')
head = ListNode(0,ListNode(1,ListNode(2)))
printLN(head)
printLN(rotateRight(head, 4))
print('-----')
head = ListNode(1,ListNode(2))
printLN(head)
printLN(rotateRight(head, 3))
print('-----')
head = ListNode(1,ListNode(2, ListNode(3)))
printLN(head)
printLN(rotateRight(head, 2000000000))
