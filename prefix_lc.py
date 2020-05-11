class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre=""
        if not len(strs):
            return pre
        for i in xrange(len(min(strs):
            c=strs[0][i]
            if all(a[i]==c for a in strs):
                pre+=c
            else:
                return pre
        return pre
