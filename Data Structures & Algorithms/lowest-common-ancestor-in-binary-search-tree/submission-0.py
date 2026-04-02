# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            else:
                return curr     




# since it is a binary search tree, meaning that the left side tree always small than
## right side 

# check the p and q is both larger than current node or not
## if larger, traverse to right sie 
## else, to left side 
