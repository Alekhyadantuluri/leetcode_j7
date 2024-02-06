class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l1=[]
        for i in strs:
            l1.append(''.join(sorted(i)));
        a = []
        for i in range(len(l1)):
            if l1[i] !=0:
                k=[strs[i]]
                for j in range(i+1,len(l1)):
                    if l1[i]==l1[j]:
                        k.append(strs[j])
                        l1[j]=0
                l1[i]=0
                a.append(k)
        a.sort()
        return a
                                 
