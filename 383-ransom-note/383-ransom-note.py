class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d={}
        count=1        
        
        
        for i in ransomNote:
            if i not in d:
                d[i]= count
            elif i in d:
                d[i]+= 1
            if d[i] > magazine.count(i):
                return False
        return True
            