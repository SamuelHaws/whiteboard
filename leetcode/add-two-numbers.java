/**
* Runtime: 2 ms, faster than 79.75% of Java online submissions for Add Two Numbers.
* Memory Usage: 43.5 MB, less than 88.09% of Java online submissions for Add Two Numbers. (varied, ~42MB)
*/

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode pSum = new ListNode(0);
        ListNode pHead = pSum;
        boolean carryFlag = false;
        int onesDigit = 0;
        int sum = 0;
        
        while (l1 != null || l2 != null) {
            if (l1 == null)
                sum = l2.val;
            else if (l2 == null) 
                sum = l1.val;
            else
                sum = l1.val + l2.val;
            
            pSum.val = carryFlag ? 1 : 0;
            
            if (pSum.val + sum == 10) {
                pSum.val = 0;
                carryFlag = true;
            }
            else if (sum < 10) {
                pSum.val += sum;
                carryFlag = false;
            }  
            else {
                onesDigit = sum % 10;
                pSum.val += onesDigit;
                carryFlag = true;
            }
            
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
            if (l1 != null || l2 != null) {
                pSum.next = new ListNode(0);  
                pSum = pSum.next;
            } else if (carryFlag) {
                pSum.next = new ListNode(1);
                pSum = pSum.next;
            }
        }
        return pHead;
    }
}