class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        a=''
        b=''
        for i in order:
            d[i]=0
        for i in s:
            if i in d.keys():
                d[i]+=1
            else:
                a+=i
        for i in d:
            b+=(i*d[i])
        return b+a
            
        