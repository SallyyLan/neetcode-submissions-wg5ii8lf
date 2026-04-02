class Solution:
    def isValid(self, s: str) -> bool:
        
        mp = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []
        for char in s:
            if char in mp:
                if stack and stack[-1] == mp[char]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(char)

        return True if not stack else False 

            









# LIFO
# what do we need:
## 1. stack = []
## 2. for loop the stack 
### set condition to check wether the input valid or not 
### - if the last char in map and stack is not empty, pop from the stack 
### - else return False 
## else add into the stack 
# return true if stack is empty else false 