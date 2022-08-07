class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        
        for i in range(len(digits)):
            digits[i]= digits[i]+1
            if digits[i] != 10:
                digits.reverse()
                return digits
            else:
                digits[i] = 0
        digits.append(1)
        digits.reverse()
        return digits
            
        
            