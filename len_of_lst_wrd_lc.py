class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        c=0
        if(s=="" or s==" "):
            return 0
        for i in range(len(s)):
            if(i==len(s)-1 and s[i]==" "):
                return c
            elif s[i].isalpha():
                count+=1
                c=count
            elif s[i]==" ":
                count=0
        return c
