class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        count=1  
        
        for i in nums:
            if i in d:
                return True
            d[i]= count
        
        return False
