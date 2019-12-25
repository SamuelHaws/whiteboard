# Runtime: 92 ms, faster than 91.80% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.

def findMedianSortedArrays(nums1, nums2):
  # merged array to find median of
  merged = [None] * (len(nums1) + len(nums2))
  # counters
  c1, c2, cMerged = (0,0,0)

  # merge nums1 and nums2 until we reach end of either
  while c1 < len(nums1) and c2 < len(nums2):
    if nums1[c1] <= nums2[c2]:
      merged[cMerged] = nums1[c1]
      c1 += 1
    else:
      merged[cMerged] = nums2[c2]
      c2 += 1
    cMerged += 1

  # add remaining elements to end of merged
  while c1 < len(nums1):
    merged[cMerged] = nums1[c1]
    c1 += 1
    cMerged += 1
  while c2 < len(nums2):
    merged[cMerged] = nums2[c2]
    c2 += 1
    cMerged += 1
  
  # calculate median
  if (len(merged) % 2 == 0):
    median = (merged[(len(merged)-1) // 2] + merged[(len(merged)-1) // 2 + 1]) / 2
  else:
    median = merged[len(merged) // 2]

  print(median)
  return median

nums1 = [1,3]
nums2 = [2]
findMedianSortedArrays(nums1, nums2)