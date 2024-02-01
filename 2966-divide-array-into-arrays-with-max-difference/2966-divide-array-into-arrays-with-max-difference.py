class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums=sorted(nums)
        l=[]
        for i in range(0,len(nums)-2,3):
            a=[nums[i]]
            if nums[i+1]-nums[i] <=k and nums[i+2]-nums[i+1]<=k and nums[i+2]-nums[i]<=k:
                a.append(nums[i+1])
                a.append(nums[i+2])
            else:
                return []
            l.append(a)
        return l
        
        