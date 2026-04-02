class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        mp = defaultdict(int)
        max_length = 0
        
        left = 0
        for right in range(len(s)):
            
            mp[s[right]] += 1

            if (right - left + 1) - max(mp.values()) > k:
                mp[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length







# sliding window 
# tracker of length 
# left and right pointer 
# calculate each char count 
# condition: total window size - the larger count <= k
## if so, move the right pointer 
## update the max length 
#