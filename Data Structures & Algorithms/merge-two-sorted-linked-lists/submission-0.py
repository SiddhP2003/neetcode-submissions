# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            ptr1, ptr2 = list1, list2
            head = ListNode()
            dummy = head

            while ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    dummy.next = ptr1
                    dummy = dummy.next
                    ptr1 = ptr1.next
                else:
                    dummy.next = ptr2
                    dummy = dummy.next
                    ptr2 = ptr2.next
            
            while ptr1:
                dummy.next = ptr1
                dummy = dummy.next
                ptr1 = ptr1.next
            
            while ptr2:
                dummy.next = ptr2
                dummy = dummy.next
                ptr2 = ptr2.next
            
            return head.next