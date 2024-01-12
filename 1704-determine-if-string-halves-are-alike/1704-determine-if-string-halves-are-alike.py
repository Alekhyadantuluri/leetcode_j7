class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=['A','E','I','O','U','a','e','i','o','u']
        i = 0
        j = len(s)-1
        o,t=0,0
        while(i<j):
            if s[i] in l:
                o+=1
            if s[j] in l:
                t+=1
            i+=1
            j-=1
        return o==t
        