class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ''
        
        count = 0
        previndex = 0
        result = ''
        for index, part in enumerate(S):
            if part == '(':
                count += 1
            else :
                count -= 1
            if count == 0:
                result += S[previndex + 1 : index]
                previndex = index + 1
        print(result)
        return result