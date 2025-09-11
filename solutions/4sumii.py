class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Brute Force
        # n = len(nums1)
        # res = 0

        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             for l in range(n):
        #                 if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
        #                     res += 1
        
        # return res

        # Use hashmap - dictionary
        # Traverse first two arrays and store the possible results and count in the hashmap

        hashmap = {} #result : count(possible combinations)
        res = 0

        for i in nums1:
            for j in nums2:
                if i + j in hashmap:
                    hashmap[i+j] += 1
                else:
                    hashmap[i+j] = 1
        
        for k in nums3:
            for l in nums4:
                key = - k - l # what we're looking for in hashmap
                if key in hashmap:
                    res += hashmap[key]
        
        return res



