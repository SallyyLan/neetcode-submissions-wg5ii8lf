# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # iterative dfs
        if not root:
            return 0

        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)

            if node.left:
                stack.append([node.left, depth + 1])

            if node.right:
                stack.append([node.right, depth + 1])

        return res 





# stack last in first out concept to achieve 
# we store the previous node and its depth to traverse further of the tree 

# what do we need 
## base case:
### if the root is non -> return 0 

## recursive call 
## initilaize the stack, put the root and depth in it as the start 
## initilaize a tracker for the length 

# we continuly pop the node in the stack to check whether they have child 
# when the curr is not empty: 
## first pop the last element in the stack 
## if the node is valid, update the length tracker 
## if the element left is valid, we further append their left child
## if the element right is valid, we append right child 

# at the end we return the length tracker 













