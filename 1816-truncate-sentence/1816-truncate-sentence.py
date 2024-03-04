class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ns=''
        for i in range(len(s)):
            if s[i]==' ':
                k-=1
            if k==0:
                return ns
            ns=ns+s[i]
        return ns
        
        
            
        