class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        count=0
        l=[]
        n=''
        a=x
        if x >= 0 and x < 10:
            return True
        elif x > 0:
            while x > 0:
                count = count + 1
                digit=str(x%10)
                n=n+digit
                x = x//10
            n = (int(n))
            if n==a:
                return True
            else:
                return False
