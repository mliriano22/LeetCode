class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        answer=[] # the array we will return
        
        left=1 #need to initialize with 1 for mulitplication purposes 
        right=1
 
        
        for i in range(len(nums)):
            answer.append(left) # first we append as to not include the first number then we can multiply
            left =left*nums[i] 
            
            
        for j in range(len(nums)-1,-1,-1): #backwards version of our previous loop
            answer[j]=answer[j]*right # multiplies the correct indices in our answer array 
            right= right*nums[j]
            
        return answer
            
        
            
        
            
            
                
            