class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        l=[]
        for i in range(len(n)):
            l.append(p[i])
            l.append(n[i])
        return l
        