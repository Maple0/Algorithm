
class Solution:
    def findDiagonalOrder(self,mat):
        m=len(mat)-1
        n=len(mat[0])-1
        direct=0 #1: up 0:down
        isChanging=1 # if changing direction
        res=[mat[0][0]]

        i,j=0,0
        while 1:
            if i==m and j==n:
                break
            #current direction is UP
            if direct ==1:
                if isChanging==1:
                    if i+1 <= m:
                        i=i+1
                    else:
                        j=j+1    
                    res.append(mat[i][j])
                    isChanging=0
                    continue
                if i-1>=0 and j+1 <=n:
                    res.append(mat[i-1][j+1])
                    i=i-1
                    j=j+1
                    continue
                else:
                    direct=0
                    isChanging=1
                    
            #current direction is DOWN
            if direct ==0:
                if isChanging==1:
                    if j+1<=n:
                        j=j+1
                    else:
                        i=i+1
                    res.append(mat[i][j])    
                    isChanging=0
                    continue
                if i+1<=m and j-1 >=0:
                    res.append(mat[i+1][j-1])
                    i=i+1
                    j=j-1
                else:
                    direct=1
                    isChanging=1
        return res

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().findDiagonalOrder(mat))