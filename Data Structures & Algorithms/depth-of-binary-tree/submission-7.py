# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # BFS
        if not root:
            return 0

        queue = deque([root])
        level = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

        return level 



# BFS -> queue (first in first out)
# search layer by layer and track the level 

# base case: if the root is non, return 0 
# problem: how do we know we have move to the next level?
## for loop the length of current queue
# since we will pop the element from the beginning, the number of element in the queue
## is the amount of how much node in that layer. 

# for loop the queue
## popleft the element 
## if the num.left is valid, append 
## if the num.right is valid, append 

# tracker += 1

# return the tracker 