# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level:
                res.append(level)

        return res 








# BFS, level by level, queue, first in first out 
# how do we know we should move to next level -> for loop the length of queue 

# initialize a res of list 
# queue put the root in it 
# while queue, for loop the queue, pop the node, check the node, put the node into the 
## temp list for putting into the result, then append its left and right into the queue