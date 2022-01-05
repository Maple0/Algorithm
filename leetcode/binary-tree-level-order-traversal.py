#Author: Maple0
#Github:https://github.com/Maple0
#9th Sep 2016

#Given a binary tree, return the level order traversal of its nodes' values. 
#(ie, from left to right, level by level).
#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its level order traversal as:
#[
#  [3],
#  [9,20],
#  [15,7]
#]

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrder(self,root):
		res,next=[],[]
		if root:
			temp=[root]
		else:
			return res
		res.append(temp)
		
		while 1:
			for v in temp:
				if v.left:
					next.append(v.left)                
				if v.right:
					next.append(v.right)     
			if next==[]:
				break
			res.append(next)
			temp=next
			next=[]
		return [[v.val for v in x] for x in res]
		
node1=TreeNode(3)
node2=TreeNode(9)
node3=TreeNode(20)
node4=TreeNode(15)
node5=TreeNode(7)
node6=TreeNode(11)
node7=TreeNode(6)
node8=TreeNode(8)

node1.left=node2
node2.left=node6
node2.right=node7
node1.right=node3
node3.left=node4
node3.right=node5
node5.right=node8

#       3
#    /     \
#   9      20
#  /  \    /  \
# 11   6   15  7
#               \
#				 8
r=Solution().levelOrder(node1)
print(r)
  