class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} #{val:idx}
        
        for idx,val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return [idx, seen[diff]]
            seen[val] = idx
