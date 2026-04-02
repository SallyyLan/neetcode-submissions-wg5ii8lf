class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        sort_no_dup = sorted(set(nums))

        max_length = 1
        cur_length = 1

        for i in range(1, len(sort_no_dup)):
            if sort_no_dup[i] == sort_no_dup[i - 1] + 1:
                cur_length += 1
            else:
                cur_length = 1

            max_length = max(max_length, cur_length)
        
        return max_length

            
