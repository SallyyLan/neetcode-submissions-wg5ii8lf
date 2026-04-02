class Solution:
    def isValid(self, s: str) -> bool:
        

        mp = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []
        for char in s:
            if char not in mp:
                stack.append(char)
            else:
                if stack and stack[-1] == mp[char]:
                    stack.pop()
                else:
                    return False 

        return True if not stack else False

