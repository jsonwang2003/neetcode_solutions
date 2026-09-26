class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        groups = {}

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            
            key = ",".join(map(str, chars))
            
            if key in groups.keys():
                groups[key].append(s)
            else:
                groups[key] = [s]
            
        for key in groups.values():
            output.append(key)

        return output