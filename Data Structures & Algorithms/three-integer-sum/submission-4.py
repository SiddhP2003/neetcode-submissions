class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low, high = i + 1, len(nums) - 1
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                if total == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                elif total > 0:
                    high -= 1
                else:
                    low += 1
        
        return res
                