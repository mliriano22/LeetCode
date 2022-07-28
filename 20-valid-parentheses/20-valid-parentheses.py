class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        open=[]

        if s.count("{") != s.count("}") or s.count("[") != s.count("]") or s.count("(") != s.count(")"):
            return False

        for i in range(len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                open.append(s[i])
            
            if len(open) ==0:
                continue

            if s[i] == "]" and open[-1]== "[":
                open.pop()

            if s[i] == "}" and open[-1]== "{":
                open.pop()

            if s[i] == ")" and open[-1]== "(":
                open.pop()

        if len(open) >0:
            return False

        return True
