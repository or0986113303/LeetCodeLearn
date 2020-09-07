class Solution(object):
    def dfstraversalofallsubset(self, leftindex, rightindex, result, resulttmp):
        if leftindex == 0 and rightindex == 0:
            result.append(resulttmp)
            return
        if leftindex > 0:
            self.dfstraversalofallsubset(leftindex - 1, rightindex, result, resulttmp + '(')
        if leftindex < rightindex:
            self.dfstraversalofallsubset(leftindex, rightindex - 1, result, resulttmp + ')')

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # assume result is a standard binary tree
        # which can be split two parts about left part and right part
        if not n :
            return []
        elif n == 0 :
            return []
        elif n == 1:
            return ['()']
        result = []
        self.dfstraversalofallsubset(n, n, result, '')
        return result


        
if __name__ == "__main__":
    n = 3
    idealresult = ["((()))", "(()())", "(())()", "()(())", "()()()" ]
    result = Solution().generateParenthesis(n)
    print(result)
    assert result == idealresult, False