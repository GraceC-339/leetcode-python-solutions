class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # store the magazine letter:frequency in dictionary
        mag_map = {}

        for l in magazine:
            mag_map[l] = mag_map.get(l , 0) + 1
        
        # traverse the ransomNote, and check if the letters in magazine

        for l in ransomNote:
            if l in mag_map and mag_map[l] > 0:
                mag_map[l] -= 1
            else:
                return False
        
        return True