class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # sort the car by position
        # calculate the time for each car to get to the target

        pair = [[p,s] for p,s in zip(position, speed)]

        stack = []

        for p,s in sorted(pair)[::-1]: #Reversed sorted order
            time = (target - p)/s # decimal division
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

            


