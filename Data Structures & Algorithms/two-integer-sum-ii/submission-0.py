class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #brute force 
        # try every combination and find with two indices add up to target 
        # return list of indices + 1 
        # O(n^2)
        # O(1)

        #optimal solution 
        # two pointers
        # l,r = 0, len(numbers) - 1
        # O(n) time O(1) space 
        l,r = 0, len(numbers) - 1
        while l < r:
            if (numbers[l] + numbers[r]) == target:
                return [l + 1, r + 1]
            elif (numbers[l] + numbers[r]) > target:
                r-=1
            else:
                l += 1
        return [-1, -1]
    