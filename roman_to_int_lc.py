class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        values={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        for i in range(len(s)):
            val=values[s[i]]
            if i+1<len(s) and values[s[i+1]] > val:
                sum-=val
            else:
                sum+=val
        return sum
