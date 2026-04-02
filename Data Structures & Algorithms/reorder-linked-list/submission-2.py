# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head:
            return 

        cur_list = []
        cur = head 
        while cur:
            cur_list.append(cur)
            cur = cur.next

        left, right = 0, len(cur_list) - 1
        while left < right:
            cur_list[left].next = cur_list[right]
            left += 1

            if left >= right:
                break

            cur_list[right].next = cur_list[left]
            right -= 1


        cur_list[left].next = None



