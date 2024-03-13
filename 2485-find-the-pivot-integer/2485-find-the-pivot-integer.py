class Solution:
    def pivotInteger(self, n: int) -> int:
        a = (n*(n+1))//2
        b = n
        i=n
        while(i>0):
            if a==b:
                return i
            a-=i
            b+=(i-1)
            i-=1
        return -1