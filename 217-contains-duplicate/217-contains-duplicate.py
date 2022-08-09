class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        count=1
        
        
        
        for i in nums:
            if i not in d:
                d[i]= count
            elif i in d:
                return True
        return False
