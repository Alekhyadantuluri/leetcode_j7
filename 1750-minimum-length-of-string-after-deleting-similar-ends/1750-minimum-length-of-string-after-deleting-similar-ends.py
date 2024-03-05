class Solution:
    def minimumLength(self, s: str) -> int:
        # k=len(s)
        i=0
        j=len(s)-1
        # mt=''
        while(i<j):
            if s[i]==s[j]:
                while(i+1<j and s[i]==s[i+1]):
                    i+=1
                while(i<j-1 and s[j]==s[j-1]):
                    j-=1
                i+=1
                j-=1
            else:
                return j-i+1
        return j-i+1
                    
        