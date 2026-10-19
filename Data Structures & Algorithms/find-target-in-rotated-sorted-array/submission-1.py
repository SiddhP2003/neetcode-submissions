class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #brute force 
        # look through array and find nums 
        # O(N)

        #optimal solution O(log n)
        # binary search 
        # [4,5,6,7,0,1,2]
        # [0,1,2,4,5,6,7]
        # k = 3 
        # [4,5,6,7, nums[k]...]
        # low, mid, high 
        # rotated or not rotated part of array depending on if nums[m] > nums[l] 
        # if nums[m] > nums[l] not rotated otherwise it is rotated 
        # target < nums[l] 
        # low = mid + 1 

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2 
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1 
                else:
                    high = mid - 1
            else: 
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1