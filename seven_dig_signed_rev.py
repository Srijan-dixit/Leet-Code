class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        x_pos=abs(x)
        INT_MAX= 2**31 -1
        INT_MIN= -2**31
        while x_pos:
            rem = x_pos%10
            x_pos /= 10
            if (rev > INT_MAX/10) or (rev == INT_MAX / 10 and rem > 7):
                return 0
            rev = rev*10 + rem
        if x<0:
            rev = -rev
        return rev
