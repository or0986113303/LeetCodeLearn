class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sourcehash={}
        count=0
        first=-1
        for i in range(len(s)):
            if s[i] in sourcehash and sourcehash[s[i]] > first:
                first=sourcehash[s[i]]
            sourcehash[s[i]]=i
            count=max(count,(i-first))
        print(sourcehash)
        return count