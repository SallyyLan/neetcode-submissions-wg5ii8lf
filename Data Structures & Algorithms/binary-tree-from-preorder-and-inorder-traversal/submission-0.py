# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder and not inorder:
            return None 

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root
        







# finding the root first
## based on the natural of the preorder, the first index will be the root 
## match to the inroder list and find out the which index the root is
### based on the inorder natural, we know that it will traverse from left to right 
### thus after finding the mid, parition the list to know the left children tree and right 