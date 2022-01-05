class Solution:
    def sortedSquares(self, nums):
        square_nums=[]
        left = 0 
        right = len(nums)-1
        while left <= right: 
            if abs(nums[left]) <= abs(nums[right]): 
                square_nums.insert(0, nums[right]**2)
                right = right - 1 
            elif abs(nums[left]) > abs(nums[right]): 
                square_nums.insert(0, nums[left]**2)
                left = left + 1 
                
        return square_nums

nums = [-7,6,2,3,11]
print(Solution().sortedSquares(nums))