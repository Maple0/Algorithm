class Solution:
    def longestSubarray(self, nums):
        prev=0
        cur=0
        maxn=0

        for n in nums:
            if n ==1:
                cur+=1
            else:
                prev=cur
                cur=0
            maxn=max(maxn,cur+prev)
        if maxn == len(nums):
            maxn-=1
        return maxn

nums = [0,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0]
print(Solution().longestSubarray(nums))