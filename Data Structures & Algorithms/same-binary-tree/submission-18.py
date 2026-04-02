# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        pqueue = deque([p])
        qqueue = deque([q])
        while pqueue and qqueue:
            
            for _ in range(len(qqueue)):
                p_n = pqueue.popleft()
                q_n = qqueue.popleft()

                if not p_n and not q_n:
                    continue

                if not p_n or not q_n or p_n.val != q_n.val:
                    return False 
                
                pqueue.append(p_n.left)
                pqueue.append(p_n.right)
                qqueue.append(q_n.left)
                qqueue.append(q_n.right)

        return True 


