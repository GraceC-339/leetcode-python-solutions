# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        currA, currB = headA, headB
        sizeA = sizeB = 0

        # get the size of A and B
        while currA:
            sizeA += 1
            currA = currA.next

        while currB:
            sizeB += 1
            currB = currB.next
        
        currA, currB = headA, headB
        if sizeA > sizeB:
            diff = sizeA - sizeB
            for _ in range(diff):
                currA = currA.next
            while currB:
                if currA == currB:
                    return currA
                currA = currA.next
                currB = currB.next
        elif sizeA < sizeB:
            diff = sizeB - sizeA
            for _ in range(diff):
                currB = currB.next
            while currA:
                if currA == currB:
                    return currA
                currA = currA.next
                currB = currB.next
        else:
            while currA and currB:
                if currA == currB:
                    return currA
                currA = currA.next
                currB = currB.next
        
        return None

            


