class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        o=1
        s=2
        if n==1:
            return 1
        elif n==2:
            return 2
        for i in range(3,n+1):
            t=o+s
            o=s
            s=t
        return t
