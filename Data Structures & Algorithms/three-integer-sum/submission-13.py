class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for z in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[z] == 0:
                        temp = [nums[i], nums[j], nums[z]]
                        res.add(tuple(temp))

        return [list(i) for i in res]







# similar to two sum 
# calculate the difference and check whether the difference 
## exist in the map 
# using map because we need the index of that number 
## map can achieve O(1) look up 

# also, since the output should not contain duplicate 
## using set() to prevent that 
## but remember we should return list at the end 

# to achieve this, we can brute force is by using triple for loop
## but that will be O(n3)

# the optimal solution is using one for loop with two pointer
## using two pointers we should ensure the list is sorted 