class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        list=[1,5,10,50,100,500,1000]
        list2=['I','V','X','L','C','D','M']
        d={}
        count=0
        n=0
        for i in list2:
            count=count+1
            d[i]=list[count-1]
        if len(s)==1:
            n=d[s[0]]
        else:
            for j in range(len(s)):
                if j == 0 and d[s[j + 1]] >= d[s[j]]:
                    n=n+d[s[j]]
                elif j == 0 and d[s[j + 1]] < d[s[j]]:
                    n=n+d[s[j]]
                elif j>0 and d[s[j-1]] >=d[s[j]]:
                    n=n+d[s[j]]
                else:
                    n=n+d[s[j]]-d[s[j-1]]*2
        return n