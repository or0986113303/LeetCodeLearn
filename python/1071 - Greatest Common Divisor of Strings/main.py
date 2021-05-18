# There is just the repeat characters to combine a string one
# and given a string two to find the greater common divisor
# So we can assume the gcd be happened at the shorter one and just use the length gcd to decide the result
class Solution(object):
    def gcd(self, source1, source2):
            return source1 if source2 == 0 else self.gcd(source2, source1 % source2)
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m, n = len(str1), len(str2)
 
        # solution two
        if str1 + str2 != str2 + str1:
            return ""
 
        return str1[:self.gcd(m, n)]
        