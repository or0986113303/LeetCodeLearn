class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for parts in S:
            if parts in J:
                result += 1
        return result

if __name__ == "__main__":
    J = 'aA'
    S = 'aAAbbbb'
    idealresult = 3
    result = Solution().numJewelsInStones(J, S)
    print(result)
    assert result == idealresult, False