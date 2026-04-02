class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        seen = set()
        max_len = 0
        cur_len = 0

        left = 0
        for right in range(len(s)):
            if s[right] not in seen:
                cur_len += 1
                seen.add(s[right])

            else:
                while s[right] in seen and left < right:
                    seen.remove(s[left])
                    left += 1
                    cur_len -= 1

                seen.add(s[right])
                cur_len += 1

            max_len = max(max_len, cur_len)

        return max_len



# use sliding window to find the longest substring 
# to avoid the duplicate -> using set 
# variable for tracking the max 
# variable for tracking the current 

# initialize the left pointer 
# for loop the right pointer for expanding and shrinking the window
# check whether the current char in set or not 
# if not, current += 1
# update the max length
# if char in set, set while loop for keep remove the duplicate from left pointer 
## check if the left pointer < right pointer, left += 1 while removing 

# return max_length 