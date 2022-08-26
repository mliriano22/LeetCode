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
            d[i]=ransomNote.count(i)
            if d[i] > magazine.count(i):
                return False
        return True
            