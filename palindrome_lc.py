class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev=0
        x_temp=x
        val=False
        while x_temp and x>=0:
            rem = x_temp % 10
            x_temp /= 10
            rev = rev*10 + rem
        if rev==x:
            val=True
        return val
