# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        stack = [(p, q)]

        while stack:
            p_, q_ = stack.pop()

            if not p_ and not q_:
                continue

            if not p_ or not q_ or p_.val != q_.val:
                return False 
            
            stack.append((p_.left, q_.left))
            stack.append((p_.right, q_.right))

        return True