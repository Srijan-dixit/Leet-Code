class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        for j in range(len(nums)):
            if target<nums[j]:
                return j
            elif j==len(nums)-1:
                return j+1
