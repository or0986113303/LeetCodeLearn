class Solution(object):
    stack = []
    def pushtostack(self, source):
        self.stack.append(source)
        return 'Nothing'
    def popfromstack(self, source):
        if self.stack:
            tmp = self.stack[-1]
            self.stack = self.stack[:-1]
            result = tmp + source
        else :
            result = source
        return result
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s :
            return False
        operatormap = {
            '(' : self.pushtostack,
            '[' : self.pushtostack,
            '{' : self.pushtostack,
            ')' : self.popfromstack,
            ']' : self.popfromstack,
            '}' : self.popfromstack
        }
        result = []
        for part in s:
            tmp = operatormap[part](part)
            if tmp != 'Nothing':
                if tmp == '{}' or tmp == '[]' or tmp == '()':
                    result.append(True)
                else :
                    result.append(False)
        return not False in result if len(result) > 0 else False
            
if __name__ == "__main__":
    source = ']'
    idealresult = True
    result = Solution().isValid(source)
    print(result)
    assert result == idealresult, False