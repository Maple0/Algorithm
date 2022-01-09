from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def backtrack(s,left,right):
            if len(s) == 2*n:
                res.append(s)
            else:
                if left <n:
                    backtrack(s+"(",left+1,right)
                
                if left > right:
                     backtrack(s+")",left,right+1)
        
        backtrack("",0,0)
        return res

res=Solution().generateParenthesis(2)
print(res)