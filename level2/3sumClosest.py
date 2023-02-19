class Solution:
    #time O(n^2)
    #space O(1)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum == target:
                    return curSum
                if abs(curSum - target) < abs(result - target):
                    result = curSum
                if curSum < target:j += 1
                if curSum > target: k -= 1
        return result
                

