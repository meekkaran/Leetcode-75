#O(n) time | O(n)space
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        total = 0
        for num in nums:
            total += num
            output.append(total)
        return output

