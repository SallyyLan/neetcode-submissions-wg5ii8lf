class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue 
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                three = n + nums[left] + nums[right]
                if three < 0:
                    left += 1
                elif three > 0:
                    right -= 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res 


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#         res = set()
#         nums.sort()

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for z in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[z] == 0:
#                         tmp = [nums[i], nums[j], nums[z]]
#                         res.add(tuple(tmp))

                    

#         return [list(i) for i in res]