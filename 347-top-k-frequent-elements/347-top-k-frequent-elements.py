class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        l=set()
        
        
        for i in nums:
            if i not in d:
                d[i]= 1
                if len(d) == len(nums):
                    return nums
            elif i in d:
                d[i] +=1  
        
        return heapq.nlargest(k,d.keys(),key=d.get)
        
        
                
            
        