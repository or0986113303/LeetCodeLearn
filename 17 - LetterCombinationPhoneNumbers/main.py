class Solution(object):
    digitsmap = {
        '2':['a','b','c'], '3': ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k', 'l'],
        '6':['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z']
    }
    def dfstraversalallofsubsets(self, source, result, resulttmp, startindex):
        if len(source) == startindex:
            if resulttmp != '':
                result.append(resulttmp)
            return
        
        for part in self.digitsmap[source[startindex]]:
            self.dfstraversalallofsubsets(source, result, resulttmp + part, startindex + 1)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        tmp = set(digits)
        if '1' in tmp:
            return []
        result = []
        self.dfstraversalallofsubsets(digits, result, '', 0)
        return result
        
if __name__ == '__main__':
    source = '2345'
    result = Solution().letterCombinations(source)
    print(result)
        
            