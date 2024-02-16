class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        a=sorted(list(d.values()))
        print(a)
        for i in range(len(a)):
            if k >= a[i]:
                k-=a[i]
                a[i]=0
            else:
                break
        return (len(a)-a.count(0))