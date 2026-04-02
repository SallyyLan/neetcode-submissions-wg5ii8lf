# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        node = []
        cur = head
        while cur:
            node.append(cur)
            cur = cur.next

        removeidx = len(node) - n

        if removeidx == 0:
            return head.next 

        node[removeidx - 1].next = node[removeidx].next

        return head






# since we only get the position of which node should be removed -> find the index to remove it 
# initialize a list, traverse through the linked list first then pinpoint the index 

# assign the previous node connect to the next node of the remove node 
# edge case:
## when the removeidx is 0, then we directly return the next of the head 
