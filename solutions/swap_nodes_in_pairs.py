# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
         
        # initiate a dummy head
        dummy_head = ListNode(-1, head)

        curr = dummy_head

        while curr.next and curr.next.next:
            temp = curr.next
            temp1 = curr.next.next.next
            curr.next = curr.next.next
            curr.next.next = temp
            temp.next = temp1
            curr = curr.next.next
        
        return dummy_head.next
