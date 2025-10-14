class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize result as the first element
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            # If the current subarray is already sorted, the leftmost element is the minimum
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2  # Find the middle index
            res = min(res, nums[m])  # Update result if middle element is smaller

            # If middle element is greater than or equal to the leftmost,
            # the minimum is in the right half
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # Otherwise, the minimum is in the left half
                r = m - 1

        return res