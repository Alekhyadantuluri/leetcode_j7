class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=(nums[i])**2
        # nums=sorted(nums)
        return sorted(nums)
        