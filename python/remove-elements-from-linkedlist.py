from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummyNode=ListNode(0)
        dummyNode.next=head

        prev=dummyNode
        curr=dummyNode.next

        while curr:
            if curr.val == val:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=prev.next
                curr=curr.next
        return dummyNode.next

head=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)

n4=ListNode(2)
n5=ListNode(3)
 
head.next=n2
n2.next=n3
n3.next=n4
n4.next=n5


Solution().removeElements(head,3)