class Solution:
    def maxArea(self, height: List[int]) -> int:
        #brute force 
        # two for loops 
        # start from every bar and search the bars after it and find the two bars with the most area 
        # return max area 
        # O(n^2)

        #optimal solution 
        # two pointers 
        # l,r from 0, len(height)-1
        # maxArea = 0 
        # while l < r 
        # minimum of height of l and r * (r - l) 
        # maxArea to the max of current maxArea and curArea 
        # check the next bar from each pointer, and depending on which bar is longer you would move that pointer and if equal move left 
        # O(n), O(1)
        l,r = 0, len(height) - 1
        maxArea = 0
        # maxarea : 8, 49
        while l < r:
            maxArea = max(min(height[l], height[r]) * (r - l), maxArea)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return maxArea