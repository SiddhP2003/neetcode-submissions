class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        #brute force 
        # loop through nums and set each digit as a pivot index 
        # add up values to the left and right and check to if they are equal 
        # the first index that is a pivot index that is valid return that index is it is the leftmost 
        # O(n^2)

        #optimal solution 

        # [1, 7, 3, 6, 5, 6]
        # [0, 1, 8, 11, 17, 22] left sums 
        # [27, 20, 17, 11, 6, 0]right sums 
        # loop through both and find the index at which the left and right sums are equal
        # if there is none return -1 
        # O(n) time O(n) space 
        # left_sums 0, 2, 3
        # right_sums 0, -1,0
        left_sums = []
        right_sums = []

        current_left = 0
        current_right = 0

        for i in range(len(nums)):
            left_sums.append(current_left)
            current_left += nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            right_sums.append(current_right)
            current_right += nums[i]
        
        right_sums.reverse()

        for i in range(len(nums)):
            if left_sums[i] == right_sums[i]:
                return i

        return -1