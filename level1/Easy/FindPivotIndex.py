#time O(n) | O(1)space
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)

        for idx, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return idx
            leftSum += ele
        return -1
