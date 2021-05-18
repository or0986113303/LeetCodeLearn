class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S
        elif len(S) == 0:
            return S
        
        letterstack = []
        result = ''
        for parts in S:
            if parts.isalpha():
                letterstack.append(parts)
        print(letterstack)
        for parts in S:
            if parts.isalpha():
                tmp = letterstack.pop()
                result += tmp
            else :
                result += parts
        return result
        