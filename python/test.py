def cal_changes(paid,due):
    changes=[50,20,10]
    finalchanges=[]
    if(paid<due):
        print("paid amount is insufficient ")
    elif(paid==due):
        print("no change is required")

    changeAmount=(paid*100)-(due*100)
    for c in changes:
        if(changeAmount>=c):
            cnt= int(changeAmount/c)
            finalchanges.append("{0}x{1}".format(str(c),str(cnt)))
            changeAmount=int(changeAmount % c)
    return finalchanges



def is_palindrome(num):
    tmpstr=str(num)
    start=0
    end=len(tmpstr)-1
    while start < end:
        if(tmpstr[start]!=tmpstr[end]):
            return False
        start+=1
        end-=1
    return True

 
class node:
     def __init__(self,val) -> None:
         self.val=val
         self.left= None
         self.right=None
#       3
#    /     \
#   9      20
#  /  \    /  \
# 11   6   15  7
#               \
#				 8
class solution:
    def level_order(self,root):
        res,next=[],[]
        if not root:
            return res
        tmp=[root]
        res.append(tmp)
        
        while True:
            for n in tmp:    
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            if next ==[]:
                break       
            res.append(next)
            tmp=next
            next=[]
        
        return [[v.val for v in n] for n in res]

node1=node(3)
node2=node(9)
node3=node(20)
node4=node(15)
node5=node(7)
node6=node(11)
node7=node(6)
node8=node(8)

node1.left=node2
node2.left=node6
node2.right=node7
node1.right=node3
node3.left=node4
node3.right=node5
node5.right=node8
res=solution().level_order(node1)
print(res)
