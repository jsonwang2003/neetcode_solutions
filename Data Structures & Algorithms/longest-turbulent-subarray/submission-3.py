class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if(len(arr) == 1):
            return 1
        if(len(arr) == 2):
            return 2 if arr[0] != arr[1] else 1

        count = 2
        maxCount = 2

        for i in range(2, len(arr)):
            l, m, r = arr[i-2], arr[i-1], arr[i]
            if(m == r):
                maxCount = max(maxCount, count)
                count = 1
            elif(l < m and m > r):
                count += 1
            elif(l > m and m < r):
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 2
        
        return max(maxCount, count)