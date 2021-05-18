import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sourcecounter = collections.Counter(s)
        targetcounter = collections.Counter(t)
        return sourcecounter == targetcounter
        