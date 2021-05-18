class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = intervals + [newInterval]
        result.sort()
        
        operatorindex = 1
        
        while operatorindex < len(result):
            if result[operatorindex][0] <= result[operatorindex - 1][1]:
                tmp = [[result[operatorindex - 1][0], max(result[operatorindex - 1][1], result[operatorindex][1])]]
                result = result[:operatorindex - 1] + tmp + result[operatorindex + 1:]
            else :
                operatorindex += 1
        return result
        
if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    idealresult = [[1,2],[3,10],[12,16]]
    result = Solution().insert(intervals, newInterval)
    print(result)
    assert result == idealresult