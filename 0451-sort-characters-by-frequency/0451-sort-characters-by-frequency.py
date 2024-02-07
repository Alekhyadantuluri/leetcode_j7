class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        l=""
        for i in s:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1

        m=list(d.values())
        m.sort()
        m=m[::-1]
        for i in m:
            k=list(d.keys())[list(d.values()).index(i)]
            d[k]=-1
            l+=k*i
        return l