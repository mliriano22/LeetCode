class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        answer=[]
        
        left=1
        right=1
   
        
        
        for i in range(len(nums)):
            answer.append(left)
            left =left*nums[i]
            
            
        for j in range(len(nums)-1,-1,-1):
            answer[j]=answer[j]*right
            right= right*nums[j]
            
        return answer
            
        
            
        
            
            
                
            