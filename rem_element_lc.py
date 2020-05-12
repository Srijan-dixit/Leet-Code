class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=[]
        for i in range(len(nums)):
            if nums[i]==val:
                j.append(i)
        j=sorted(j,reverse=True)
        for k in j:
            del nums[k]
        return len(nums)
