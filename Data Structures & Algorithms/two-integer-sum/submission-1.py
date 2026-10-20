class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # brute force 
        # nested for loop and try every possible combination of numbers 
        # when you find the first combination that works return the indices 
        # O(n^2)

        #optimal solution 
        # hashmap and store the indices with the value in the array as a key 
        # loop through nums once and check to see if target - nums[i] is already in the hashmap 
        # if it is not add the current value and its index to the map 
        # if it is return the index from the hashmap and current index 

        indices = {}

        for i in range(len(nums)):
            if target - nums[i] in indices:
                return [indices.get(target - nums[i]), i]
            else:
                indices[nums[i]] = i
        
        return -1