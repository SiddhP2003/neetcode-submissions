class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        # brute force would be o(n^3) to find three values equal to 0
        # loop through nums 
        # for every value in nums 
        # run two sum using pointers to find two values that equal to 0 that are equal to the opposite of the first value 
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0:
                    l = l + 1
                elif threeSum > 0:
                    r = r - 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
    
            
