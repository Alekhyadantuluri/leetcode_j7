class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def dictionary(n):
            d={}
            for i in n:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
            return d
        s = dictionary(s)
        t = dictionary(t)
        c = 0
        for i in t:
            if i in s.keys() and t[i]>s[i]:
                c+=(t[i]-s[i])
            elif i not in s.keys():
                c+=t[i]
        return c
        