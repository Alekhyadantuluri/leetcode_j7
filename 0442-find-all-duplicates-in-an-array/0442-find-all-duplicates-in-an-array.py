class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        duplicate=[]
        for i in nums:
            if i in d:
                duplicate.append(i)
            else:
                d[i]=1
        return duplicate