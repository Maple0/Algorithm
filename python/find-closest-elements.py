
class Solution:
    def findClosestElements(self, arr, k, x):
        res=[]
        left=0
        right=len(arr)-1
        if(len(arr)==0 or len(arr)< k):
            return res
        
        element_to_del= len(arr)-k
        for i in range(0,element_to_del):
            #print(x,arr[left],arr[right])
            if x-arr[left] <= arr[right]-x:
                right-=1
            else:
                left+=1
        return arr[left:right+1]

arr = [0, 1, 2, 3, 3, 4, 7, 7, 8]
k = 3
x = 5
print(Solution().findClosestElements(arr,k,x))