class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sourcetmp = ''
        result = []
        for part in digits:
            sourcetmp += str(part)
        sourcetmp = str(int(sourcetmp) + 1)
        for part in sourcetmp:
            result.append(part)
        return result
        