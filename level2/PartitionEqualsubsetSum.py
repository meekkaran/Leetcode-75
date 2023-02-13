#example1
class Solution:
    def canPartition(self, nums):
        nums.sort(reverse=True)
        def helper(start, target):         # Here path is not needed
            if target < 0: return
            elif target == 0: return True
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]): return True
            return False

        return False if sum(nums)%2 else helper(0, sum(nums)/2)
 

# example2
if target in d: return d[target] 
        if target == 0: d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in range(ind, n):
                    if self.canFindSum(nums, target - nums[i], i+1, n, d):
                        d[target] = True
                        break
        return d[target]
    
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0: return False
        return self.canFindSum(nums, s/2, 0, len(nums), {})
