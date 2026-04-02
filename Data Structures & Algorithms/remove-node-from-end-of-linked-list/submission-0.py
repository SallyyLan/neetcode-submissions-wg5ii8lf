# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        if not head:
            return []

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







# since we got the position of which node should be removed but don't know 
## exactly which one -> have to find out the index for positioning 

# to position the node, have to traverse the linked list first and store in the 
## array for removing 

# create a list for storing the node and traverse the linked 
# find the index to remove -> start from the end, so the total len - the n -> the position
# point to the one before the position link to the next node of the removed position