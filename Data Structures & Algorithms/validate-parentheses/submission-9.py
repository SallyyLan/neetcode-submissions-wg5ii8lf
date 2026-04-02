class Solution:
    def isValid(self, s: str) -> bool:

        mp = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []
        for char in s:
            if char in mp:
                stack.append(char)

            else:
                if not stack:
                    return False 
                
                if mp[stack[-1]] == char:
                    stack.pop()
                else:
                    return False 

        return not stack 
            


# class Solution:
#     def isValid(self, s: str) -> bool:
        
#         mp = {
#             ']' : '[',
#             '}' : '{',
#             ')' : '('
#         }

#         stack = []
#         for char in s:
#             if char in mp:
#                 if stack and stack[-1] == mp[char]:
#                     stack.pop()
#                 else:
#                     return False 
#             else:
#                 stack.append(char)

#         return True if not stack else False 




# LIFO
# stack = []
# pop()
# map