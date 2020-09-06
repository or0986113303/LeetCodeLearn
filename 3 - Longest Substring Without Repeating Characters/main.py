class Solution(object):
    def windowslide(self, source, capacity):
        operatorindex = 0
        firstoccuredindex = -1
        substringhash = {}
        maxlength = float('-inf')
        while operatorindex < capacity:
            if source[operatorindex] in substringhash and substringhash[source[operatorindex]] > firstoccuredindex:
                firstoccuredindex = substringhash[source[operatorindex]]
            substringhash[source[operatorindex]] = operatorindex
            maxlength = max(maxlength, operatorindex - firstoccuredindex)
            operatorindex += 1
        return maxlength
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        elif len(s) <= 1:
            return len(s)
        
        capacity = len(s)
        
        return self.windowslide(s, capacity)