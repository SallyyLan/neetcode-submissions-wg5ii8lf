# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        stack = [[root, 1]]
        res_depth = 0
        while stack:
            num, depth = stack.pop()

            if num:
                res_depth = max(res_depth, depth)

                stack.append([num.left, depth + 1])
                stack.append([num.right, depth + 1])

        return res_depth





# iterative dfs stack 
# first pinciple of stack: last in first out, based on previous node depth to increment 
# dive deep to the end of the tree and track the max depth 

# initialize a stack 
# put the root in it if exists 
# while the stack is not empty -> we can keep exploring 
# pop the newest node first, if the number exists, we first update the max length to the newest node depth
# then push the current node left and right into the stack and append depth + 1
# return the res 