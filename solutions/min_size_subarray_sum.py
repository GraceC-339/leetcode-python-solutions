class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
      # understand what the left and right pointer do
      # right pointer to collect the elements 
      # left pointer to find the min length of sub array

        left, right = 0, 0
        cur_sum = 0
        sub_len = float('inf')

        while right < len(nums) :
            cur_sum += nums[right]
            while cur_sum >= target:
                sub_len = min(sub_len, right-left+1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        
        return sub_len if sub_len != float('inf') else 0
