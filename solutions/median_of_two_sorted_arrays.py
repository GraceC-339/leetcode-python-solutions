class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure A is the shorter array
        if len(B) < len(A):
            A, B = B, A
        
        # Use binary search on A (the shorter array)
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # middle index of A (i is the rightmost index of the left partition of A)
            j = half - i - 2  # j is the rightmost index of the left partition of B

            # take care of the edge cases
            leftA = A[i] if i >= 0 else float("-infinity")
            rightA = A[i+1] if (i+1) < len(A) else float("infinity")
            leftB = B[j] if j >= 0 else float("-infinity")
            rightB = B[j+1] if (j+1) < len(B) else float("infinity")

            if leftA <= rightB and leftB <= rightA:  # correct partition
                # return the median depending on odd or even number of total elements
                if total % 2:  # odd total: median is the min of the right partition
                    return min(rightA, rightB)
                # even total: median is the average of max of left partition and min of right partition
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1
