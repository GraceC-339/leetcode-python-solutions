from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # fix the first number and use two pointer to search for the rest two
        # sort the nums first

        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i]>0:
                return res
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1 # don't forget to move the left pointer
                    # if the 2nd value is duplicate, jump to the next one
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        
        return res
                

