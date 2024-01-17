class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=list(d.values())
        print(l)
        print(len(set(l)))
        print(len(l))
        return len(set(l))==len(l)
        