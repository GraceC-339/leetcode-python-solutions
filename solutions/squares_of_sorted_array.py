class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Intuitive solution(Brute Force):

        nums_square = [n*n for n in nums]
        nums_square.sort()

        return nums_square

        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)

----------------
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two Pointer

        i,j,k = 0, len(nums)-1, len(nums)-1
        res = [0]* len(nums)

        while i <= j:
            squared_i, squared_j = nums[i]*nums[i], nums[j]*nums[j]
            if squared_i > squared_j:
                res[k] = squared_i
                i += 1
            else:
                res[k] = squared_j
                j -= 1
            k -= 1
        
        return res




