class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if(len(arr) < 3):
            return len(arr)

        count = 2
        maxCount = 2

        for i in range(2, len(arr)):
            l, m, r = arr[i-2], arr[i-1], arr[i]
            if(l < m and m > r):
                count += 1
            elif(l > m and m < r):
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 2
        
        return max(maxCount, count)