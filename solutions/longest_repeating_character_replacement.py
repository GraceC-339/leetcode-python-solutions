class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # frequency map for characters in the current window
        count = {}
        # maximum valid substring length found
        res = 0

        # left pointer of the sliding window
        l = 0

        for r in range(len(s)):
            # include s[r] in the window
            count[s[r]] = 1 + count.get(s[r], 0)

            # if more than k replacements are needed to make all chars equal,
            # shrink the window from the left until it's valid again
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # update result with current window size
            res = max(res, (r - l + 1))

        return res
