class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        c = 0
        i = 0
        while(k>0):
            nums = sorted(nums)
            nums[0]=nums[0]*-1
            k-=1
        return sum(nums)
        # for i in range(len(nums)):
        #     if nums[i]<=0:
        #         k-=1
        #         nums[i]=-1*nums[i]
        #         c = i
        #     elif nums[i]>0:
        #         if c!=0:
        #             nums[c]=-1*nums[c]
        #             k-=1
        #         elif k%2!=0:
        #             nums[i]=-1*nums[i]
        #             k-=1
        #         else:
        #             k-=2
        #     if k == 0:
        #         break
        # return sum(nums)
                
            
            
        