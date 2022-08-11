class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=0
        pivot=0
        
        for i in range(len(nums)):
            if ls == sum(nums[i+1:]):
                pivot= i
                return pivot
            ls= nums[i]+ls
            
        return -1
            
            
            
          
        