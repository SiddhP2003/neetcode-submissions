class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        res = [1] * (len(nums))
        # [1, 1, 2, 6]
        # [24, 12,4, 1]
        left = 1
        right = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
    
        return res
