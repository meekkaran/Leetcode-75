class Solution:
    def climbStairs(self, n: int) -> int:   
        # O(n) time and O(1) space complexity 
        if n <= 2: return n
        prev1 = 1
        prev2 = 2
        curr = 0
        for i in range(2,n):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return curr

        #solution2 
        #using a dictionary to store values already computed(memoization)
        memo = {}
        memo[1] = 1
        memo[2] = 2
        def climb(n):
            if n in memo:
                 return memo[n]
            else:
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]
        return climb(n)
        


       
