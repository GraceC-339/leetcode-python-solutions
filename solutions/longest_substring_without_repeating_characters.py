class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use sliding window to find longest substring without repeating characters.
        # Maintain a set to quickly check for duplicates in the current window.
        charSet = set()

        # l and r are the left and right indices of the sliding window.
        l = 0
        res = 0

        for r in range(len(s)):
            # If s[r] is already in the set, shrink the window from the left
            # until the duplicate is removed.
            while s[r] in charSet:
                # Remove the leftmost character from the set and move left pointer.
                charSet.remove(s[l])
                l += 1
            # Add the new character to the current window set.
            charSet.add(s[r])
            # Update result with the current window size.
            res = max(res, r - l + 1)
        
        return res

# Time complexity: O(n) — each character is added/removed at most once.
# Space complexity: O(min(n, m)) where m is size of character set (alphabet).
