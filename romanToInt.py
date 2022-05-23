class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        o = 0
        vals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        while i < len(s):
            f=0
            if i+1<len(s) and vals[s[i]] < vals[s[i+1]]:
                o=o+vals[s[i+1]]-vals[s[i]]
                i+=1
            else:
                o+=vals[s[i]]
            i+=1
        if(i<len(s)):
            o += vals[s[-1]]
        return o