# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return None

        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right 





# iterative dfs - stack, while, pop 
# first check the root is available or not 
# assign a varaibel for tracking root 
# while loop the stack and curr, ensure there's componenets in it 
# go through the left first, check whether the node exist 
# if so, pop the item 
# decrement the k 
# check if k == 0, if so return the node 
# else go through the right side 










