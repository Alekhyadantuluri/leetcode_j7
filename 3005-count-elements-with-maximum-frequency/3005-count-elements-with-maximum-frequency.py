class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        c = 0
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        maxi=max(d.values())
        for i in d:
            if d[i]==maxi:
                c+=d[i]
        return c