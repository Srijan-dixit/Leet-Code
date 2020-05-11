class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        top="#"
        start=[]
        map_={")":"(","]":"[","}":"{"}
        for i in s:
            if i in map_:
                if start:
                    top=start.pop()
                if map_[i] != top:
                    return False
            else:
                start.append(i)
        return not start
