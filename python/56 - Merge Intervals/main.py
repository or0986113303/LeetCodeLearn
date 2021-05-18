class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = intervals
        operatorindex = 1
        result.sort()
        while operatorindex < len(result):
            if result[operatorindex][0] <= result[operatorindex - 1][1]:
                tmp = [[result[operatorindex - 1][0], max(result[operatorindex][1], result[operatorindex - 1][1])]]
                result = result[:operatorindex - 1] + tmp + result[operatorindex + 1 :]
            else : 
                operatorindex += 1
        return result
        
if __name__ == "__main__":
    source = [[1,3],[2,6],[8,10],[15,18]]
    idealresult = [[1,6],[8,10],[15,18]]
    result = Solution().merge(source)
    print(result)
    assert result == idealresult