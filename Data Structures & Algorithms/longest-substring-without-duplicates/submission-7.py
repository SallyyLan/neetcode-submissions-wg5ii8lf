class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        seen = set()

        left = 0
        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length












# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        

#         max_length = 0
#         seen = set()

#         left = 0 
#         for right in range(len(s)):
#             if s[right] not in seen:
#                 max_length = max(max_length, right - left + 1)
#                 seen.add(s[right])

#             else:
#                 while s[right] in seen:
#                     seen.remove(s[left])
#                     left += 1

#                 seen.add(s[right])
#                 max_length = max(max_length, right - left + 1)
                    
#         return max_length 




# return the length of the longest substring without duplicate char 
# substring is a contiguous sequence of char without duplicates 
## no need to be alphapic order 

# sliding window -> tracking contiguous logest string
# what are needed to form sliding window? 
## two pointer 
## what is the moving pointer condition? 
### -> when the right pointer char is in the set
### -> remove the left pointer char from the set 
### -> move the left pointer += 1

