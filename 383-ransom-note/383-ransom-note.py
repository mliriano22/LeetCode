class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d={}
        od={}
        count=1        
        
        
        for i in ransomNote:
            if i not in magazine:
                return False
            elif i not in d:
                d[i]= count
            elif i in d:
                d[i]+=1
                
        for j in magazine:
            if j not in od:
                od[j]= count
            elif j in od:
                od[j]+=1
        
        for i in d:
            if d[i] > od[i]:
                return False
        return True
                
        
        
            