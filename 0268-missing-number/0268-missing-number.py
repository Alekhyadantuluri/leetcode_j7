class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        n = (a*(a+1))//2
        s = sum(nums)
        return abs(n-s)
        