class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        no_dup = set(nums)
        max_length = 1
        
        for i in range(len(nums)):
            if nums[i] - 1 not in no_dup:
                
                cur = nums[i]
                cur_length = 1

                while cur + 1 in no_dup:
                    cur += 1
                    cur_length += 1

                max_length = max(max_length, cur_length)

        return max_length
                
