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

        queue = deque([root])
        level = 0

        while queue:

            for n in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            level += 1

        return level





# queue bfs
# first principle: first in first out 
# search layer by layer 

# initialize a dequeu -> popleft()
# input the root to the queue first 

# while queue:
## how to know how many node should be check? -> the length of the current queue
## extract the root out first 
## we have to check whether root has left or right children, if so, append into the queue
## after append, level += 1

## return level 







