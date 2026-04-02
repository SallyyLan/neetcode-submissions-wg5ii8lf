class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        mp = defaultdict(int)
        max_len = 0
        # cur_len = 0

        left = 0
        for right in range(len(s)):

            mp[s[right]] += 1

            if s[right] in mp:
                if (right - left + 1) - max(mp.values()) <= k:
                    max_len = max(max_len, right - left + 1)
                else:
                    mp[s[left]] -= 1
                    left += 1


        return max_len







# repeating substring -> sliding window 
# constraint: can only replace k numbers of substring 
# find out after replace -> the longest substring length 
# to find out the longest repeating char, meaning find the smaller count of char to replace it 
## can find the longest 

# to store the char freq -> map 
# initialize max_len and cur_len tracker 

# condition: the current window size - the smallest freq <= k
# update the cur_length 