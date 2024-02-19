class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums = sorted(nums)
        maxi = -1
        for i in range(1,len(nums)):
            maxi = max(maxi,nums[i]-nums[i-1])
        return maxi
            
        