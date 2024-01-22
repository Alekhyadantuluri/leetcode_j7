class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = {}
        l=[]
        n = len(nums)
        b = int((n*(n+1))/2)
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                l.append(i)
                a[i]+=1
        s = sum(list(a.keys()))
        l.append(b-s)
        return l
        
        