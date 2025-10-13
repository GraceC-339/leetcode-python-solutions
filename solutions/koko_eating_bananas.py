class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

       # use binary search to get the min k
       # in the range of 1 to max_k (max pile in piles)

        l,r = 1, max(piles)
        res = max(piles) # compare and get the smaller one

        while l <= r:
            k = (l + r) // 2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/k)
            
            if total_time <= h:
                r = k - 1
                res = min(k, res)
            
            elif total_time > h:
                l = k + 1
            
    
        return res

        # O(n log m) time, O(1) space