
import collections
from typing import Collection, List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cnt=0
        consum=0
        map=collections.defaultdict(int)
        map[0]=1
        for i in range(len(nums)):
            consum+=nums[i]
 

            if consum-k in map:
                cnt+=map[consum-k]
            map[consum]+=1
            #print(consum,cnt)

        return cnt

nums=[1,1,1]
k=2

print(Solution().subarraySum(nums,k))