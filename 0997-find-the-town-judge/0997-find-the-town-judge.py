class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d={}
        l=[]
        if n==1:
            return 1
        for i in range(len(trust)):
            l.append(trust[i][0])
            if trust[i][1] in d:
                d[trust[i][1]]+=1
                
            else:
                d[trust[i][1]]=1
        for i in d:
            if d[i]==n-1 and i not in l:
                return i
        return -1
        
        
        