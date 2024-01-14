class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def dic(n):
            d={}
            for i in n:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
            return d
        if len(word1)!=len(word2):
            return False
        word1=dic(word1)
        word2=dic(word2)
        w1k = list(word1.keys())
        w1v = list(word1.values())
        w2k = list(word2.keys())
        w2v = list(word2.values())
        if sorted(w1k)==sorted(w2k) and sorted(w2v)==sorted(w1v):
            return True
        else:
            return False
        