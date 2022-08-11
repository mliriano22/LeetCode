class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=0
        rs= sum(nums)
        pivot=0
        
        for i in range(len(nums)):
            rs= rs-nums[i]
            if ls == rs:
                pivot= i
                return pivot
            ls= nums[i]+ls
            
        return -1
            
            
            
          
        