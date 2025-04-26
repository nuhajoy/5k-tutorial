class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newArr = []
        i = 0  
        
        while i < len(nums):  
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:  
                newArr.extend([nums[i] * 2, 0])  
                i += 2  
            else:
                newArr.append(nums[i])
                i += 1
        
     

     
        temp = []
        zeros = []

        for i in range(len(newArr)):
            if newArr[i] !=0:
                temp.append(newArr[i])
            else:
                zeros.append(newArr[i])
        
        return temp+zeros
