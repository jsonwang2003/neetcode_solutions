from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1
        
        for c in t:
            if c not in chars or chars[c] <= 0:
                return False
            chars[c] -= 1

        for v in chars.values():
            if v != 0:
                return False

        return True