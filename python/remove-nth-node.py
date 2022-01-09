from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEndSingleLoop(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummynode=ListNode(0)
        dummynode.next=head

        lNode=dummynode
        rNode=dummynode
        for _ in range(n):
            rNode=rNode.next

        while rNode.next:
            lNode=lNode.next
            rNode=rNode.next
        
        lNode.next=lNode.next.next

        return dummynode.next


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        node=head
        while node:
            node=node.next
            length+=1

        dummynode= ListNode(0)
        dummynode.next=head

        node=dummynode
        for _ in range(length-n):
            node=node.next
        node.next=node.next.next
        return dummynode.next

head=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)
head.next=n2
n2.next=n3
n3.next=n4

Solution().removeNthFromEnd(head,2)