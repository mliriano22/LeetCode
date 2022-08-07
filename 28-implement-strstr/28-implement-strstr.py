class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        nl= len(needle)
        
        for i in range(len(haystack)):
            if i == "":
                return 0
            if needle not in haystack:
                return -1
            if haystack[i] == needle[0]:
                firsthalf=haystack[:i]
                if firsthalf + needle == haystack[:i+nl]:
                    return i
            
    