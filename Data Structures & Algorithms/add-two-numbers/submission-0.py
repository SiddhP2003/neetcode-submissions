# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # create new head node 
        # loop through l1 and l2 
        # take value from l1 and l2 and add if over 9 set carry to true and store sum - 10 at current node 
        # add l1.val + l2.val + carry 
        resHead = dummy = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            dummy.next = ListNode(carry % 10)
            dummy = dummy.next
            carry //= 10
        
        return resHead.next