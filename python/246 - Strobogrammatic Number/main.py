class Solution(object):
    rotatehash = {
        '0':'0', '1':'1', '6':'9', '8':'8', '9':'6'
    }
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # assume all of numbers which can be rotated 180 degree and be seem the same just below :
        # 0, 1, 6, 8, 9
        # make the hash table to map them
        result = ''
        for part in num:
            if part in self.rotatehash:
                result += self.rotatehash[part]
        return result == num[::-1]

if __name__ == "__main__":
    source = '69'
    idealresult = True
    result = Solution().isStrobogrammatic(source)
    print(result)
    assert result == idealresult, False