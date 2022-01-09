class Solution:
    def countSqures(self,matrix):
        res=0
        if(len(matrix)==0):
            return res
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if(matrix[i][j]==1):
                    #first row or first element in a row, count 1 directly
                    if i==0 or j==0:
                        res+=1
                        dp[i][j]=1
                    #second row onwards, check [i][j] as corner of squre
                    else:
                         dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                         res+=dp[i][j]
        return res

    def countSquares1(self, matrix):
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        res = 0
        dp = [([0]*n) for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    res += dp[i][j]
        return res


matrix=[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
res=Solution().countSquares(matrix)
print(res)