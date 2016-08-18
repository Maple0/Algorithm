#Author: Maple0
#Github:https://github.com/Maple0
#18th Aug 2016
#An implementation of singly linked list 
class Node:
	def __init__(self, data=None,next=None):
		self.data = data
		self.next = None

	def get_data(self):
		return self.data

class SinglyLinkedList:
	def __init__(self):
		self.root = None
		self.last = None

	def get_root_node(self):
		return self.root

	def get_last_node(self):
		return self.last

	def search_node(self,node):
		current = self.root
		if current == node:
			return current
		else:
			while current.next is not None:
				if current.next == node:
					return current.next
				current=current.next
		raise ValueError("Data not in list")

	def append_node(self,node):
		if self.root is None:
			self.root=self.last=node
		else:
			self.last.next=node
			self.last=node

	def delete_node(self, node):
		if(self.root==node):
			self.root=self.last=node.next
		else:
			current = self.root
			while current.next is not None:
				if(current.next == node):
					current.next = node.next
					node.next  = None
					if current.next is None:
						self.last = self.root
					break
				current=current.next

linkList= SinglyLinkedList()
node_a=Node("A")
node_b=Node("B")
node_c=Node("C")

linkList.append_node(node_a)
linkList.append_node(node_b)
linkList.append_node(node_c)

print(linkList.get_root_node())
print(linkList.get_last_node())

linkList.delete_node(node_c)
linkList.delete_node(node_b)
linkList.delete_node(node_a)

print(linkList.get_root_node())
print(linkList.get_last_node())


