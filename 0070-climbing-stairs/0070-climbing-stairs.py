class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n):
            if n <= 3:
                return n
            a = 2
            b = 3
            for i in range(4,n+1):
                c = a+b
                a = b
                b = c
            return c
        return fib(n)
        