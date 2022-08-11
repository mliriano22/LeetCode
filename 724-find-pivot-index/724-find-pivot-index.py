class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        pivot=0
        
        for i in range(len(nums)):
            print sum(nums[:i]), sum(nums[i+1:])
            if sum(nums[:i])==sum(nums[i+1:]):
                    pivot=i
                    return pivot
            
        return -1
          
        