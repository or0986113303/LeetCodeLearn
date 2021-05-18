class Solution(object):
    def reorganizeString(self, S):
        length = len(S)
        result = list(S)
        for index in range(0, length, 1):
            for operatorindex in range(1, length - index - 1, 1):
                if result[operatorindex] != result[operatorindex - 1] and result[operatorindex] == result[operatorindex + 1]:
                    result[operatorindex], result[operatorindex - 1] = result[operatorindex - 1], result[operatorindex]
                elif result[operatorindex] == result[operatorindex - 1] and result[operatorindex] != result[operatorindex + 1]:
                    result[operatorindex], result[operatorindex + 1] = result[operatorindex + 1], result[operatorindex]
        return ''.join(result)

if __name__ == "__main__":
    source = 'aaabb'
    idealresult = 'aba'
    result = Solution().reorganizeString(source)
    print(result)
    assert result == idealresult, False