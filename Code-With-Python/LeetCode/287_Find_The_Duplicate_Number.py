'''   UNSOLVED   '''
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = list(set(nums))
        sumOfN = sum(n)
        sumOfGivenNums = sum(nums)
        
        if len(n) == 1:
            return n[0]
        else:
            return  sumOfGivenNums - sumOfN
                
nums = list(map(int,input().split()))
print(Solution().findDuplicate(nums))