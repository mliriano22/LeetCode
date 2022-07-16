class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # this solution uses slicing instead of data mapping 
        # data mapping like a dictionary would probably be better to avoid future errors but this was just for experimentation
        
        l=[]

        # the for loop calculates x, the number needed to be added/ found to reach the target, for each element in nums
        for i in range(len(nums)):
            
            x= target- nums[i]
            
            if x in nums: #this if statement counts x
                
                count=nums.count(x)
                
                if count == 1 and x*2 == target: #this if statement makes sure we do not return the same index twice
                    continue
                    
                else:
                    
                    l.append(i) #adds to the list we created to hold the indices
                    
        return l #returns our list of indices
    