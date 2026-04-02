class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        num_zero = nums.count(0)

        if num_zero > 1:
            return [0] * len(nums)

        mul = 1
        for n in nums:
            if n != 0:
                mul *= n

        res = []
        for n in nums:
            if num_zero == 1:
                if n == 0:
                    res.append(mul)
                else:
                    res.append(0)

            else:
                res.append(mul // n)

        return res 
                   
            
