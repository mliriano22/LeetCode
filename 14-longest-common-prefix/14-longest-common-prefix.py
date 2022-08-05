class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        mini=min(strs,key=len)
        str=""
        
        for i in strs:
            if "" in strs:
                return ""
            elif i[0] != mini[0]:
                return ""
        
        strs.sort()
        for i in strs:
            for j in range(len(mini)):
                if i[j] == mini[j]:
                    str= i[:j+1]
                if i[j] != mini[j]:
                    return str
        return str
        
        