class Solution:
    def findMin(self, nums: list[int]) -> int:
        #brute force 
        # search through array until i + 1 < i and that value is the minimum 
        l,r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]