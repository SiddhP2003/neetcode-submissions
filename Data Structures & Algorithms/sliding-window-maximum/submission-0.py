class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        #brute force
        # add k values to a list 
        # find max 
        # remove first value and add new value
        # find max again 
        # repeat until there are no more values to add 
        # return list 

        #optimal solution
        # queue
        # add k value to queue
        # keep track of max 
        output = []
        q = collections.deque() #index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
