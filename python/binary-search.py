class Solution:
    def findnumber(self,nums,target):
        left=0
        right=len(nums)-1

        while left <=right:
            mid= (left+right) //2
            if(nums[mid] == target):
                return nums[mid]
            elif nums[mid] < target:
                left=mid+1
            elif nums[mid] > target:
                right=mid-1
        
        return 0


nums=[1,2,3,5,6,7,9]
target=7

print(Solution().findnumber(nums,target))

 