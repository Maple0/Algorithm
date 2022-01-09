from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r=0,0
        zero=0
        res=0
        
        while r < len(nums):
            if zero<k:
                if nums[r] ==0:
                    zero+=1
                r +=1
            
            elif nums[r] ==1:
                r+=1
            
            else:
                if nums[l] ==0:
                    zero-=1
                l+=1
            res=max(res,r-l)
        
        return res
        