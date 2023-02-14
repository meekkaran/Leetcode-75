class Solution:
    #o(n) time and space
    def rob(self, nums: List[int]) -> int:
        #dp, tabulation
        #store curr value and reuse it for future calls
        if len(nums) == 1: return nums[0]
        dp = [*nums]
        dp[1] = max(dp[0], dp[1]) #max of 
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]

