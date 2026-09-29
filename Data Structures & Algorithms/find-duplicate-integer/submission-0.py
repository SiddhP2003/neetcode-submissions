class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # slow, fast
        # 3 -> 2 -> 4
        # 2 -> 4 -> 4
        # slow, slow2
        # 2 -> 4 -> 2
        # 1 -> 3 -> 2 
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        