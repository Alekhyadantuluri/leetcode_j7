class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        if len(s)!=len(pattern):
            return False
        d={}
        for i in range(len(s)):
            if len(set(s)) != len(set(pattern)):
                    return False
            elif pattern[i] not in d.keys():
                d[pattern[i]]=s[i]
            else:
                if s[i]!=d[pattern[i]]:
                    return False
        return True
                    
        