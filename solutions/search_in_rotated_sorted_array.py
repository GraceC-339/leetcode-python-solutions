class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers for binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            # Calculate the middle index
            m = (l + r) // 2
            # Check if the middle element is the target
            if nums[m] == target:
                return m

            # Check if mid is in the left sorted portion
            if nums[m] >= nums[l]:
                # If target is not in the left sorted portion, search right
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    # Otherwise, search left
                    r = m - 1
            # Otherwise, mid is in the right sorted portion
            else:
                # If target is not in the right sorted portion, search left
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    # Otherwise, search right
                    l = m + 1

        # Target not found
        return -1
