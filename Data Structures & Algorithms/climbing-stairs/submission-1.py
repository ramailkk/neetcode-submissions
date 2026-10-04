class Solution:
    
    def climbStairs(self, n: int) -> int:

        memo = {}        
        def f(n):
            if n in memo:
                return memo[n]
            else:
                if n == 0:
                    memo[n] = 1
                elif n < 0:
                    memo[n] = 0
                else:
                    memo[n] =  f(n-2) + f(n-1)
            return memo[n]
        return f(n)
