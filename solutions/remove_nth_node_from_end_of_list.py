# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Fast and Slow pointer

        # initiate a dummy head
        dummy_head = ListNode(next=head)

        fast = slow = dummy_head

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy_head.next

        
