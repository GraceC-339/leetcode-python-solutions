class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use stack - monotonic decreasing stack to store the temp and index

        stack = [] # store pairs - [temp, idx]
        res = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            
            stack.append([t,i])
        
        return res