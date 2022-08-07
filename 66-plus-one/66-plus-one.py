class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]= digits[-1]+1
        
        if 10 not in digits:
            return digits
        
        if 10 in digits:
            for i in range(len(digits)):
                if digits[i]== 10 and digits[i]!= digits[0]:
                    digits[i]=0
                    digits[i-1]=digits[i-1]+1
                if digits[0]== 10:
                    digits[0]=0
                    digits.insert(0,1)
                    
            if 10 not in digits:
                return digits
            
            if 10 in digits:
                digits[-1]= digits[-1]-1
                return self.plusOne(digits)
            
        
            