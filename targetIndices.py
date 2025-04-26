class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        newArr=[]
        nums.sort()
        for i in range (len(nums)):
            if nums[i] == target:
                newArr.append(i)
        return newArr
