class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        win = sum(nums[:k])
        maximum = win
        for i in range(len(nums)-k):
            win= win-nums[i] + nums[i+ k]
            maximum = max(maximum,win)
            
        # print(maximum)
        return maximum / k
