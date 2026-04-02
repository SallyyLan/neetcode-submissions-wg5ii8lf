class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]

                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                elif sum_ == 0:
                    temp = [nums[i], nums[left], nums[right]]
                    res.add(tuple(temp))
                    
                    left += 1
                    right -= 1

        
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