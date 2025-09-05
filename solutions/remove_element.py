class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # fast and slow pointers
        # fast pointer is to find the numbers we want to keep (!= val)
        # slow pointer is the result array (first k of elements)

        slow , fast = 0 , 0
        size = len(nums)

        while fast <= size - 1:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
