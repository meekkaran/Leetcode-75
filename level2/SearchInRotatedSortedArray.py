class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #base case
        if not nums: return -1
        #perform binary search
        l = 0
        r = len(nums) -1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
                r = mid -1
            else:
                l = mid +1
        return -1
