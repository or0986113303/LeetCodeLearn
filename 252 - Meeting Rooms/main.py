import collections
class Solution(object):
    def intercsectioncaculater(self, source1, source2):
        if source1[0] < source2[0] and source1[1] <= source2[0]:
            return True
        elif source1[0] >= source2[1] and source1[1] > source2[1]:
            return True
        else :
            return False
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        elif len(intervals) == 1:
            return True
        sourcetmp = []
        for parts in intervals:
            sourcetmp.append(parts)
        sourcetmp.append(intervals[0])
        result = []
        for index in range(1, len(sourcetmp), 1):
            result.append(self.intercsectioncaculater(sourcetmp[index - 1], sourcetmp[index]))
            
        resulttmp = collections.Counter(result)
        return True if len(resulttmp) == 1 and True in resulttmp else False
        
if __name__ == "__main__":
    source = [[0,30],[5,10],[15,20]]
    result = Solution().canAttendMeetings(source)
    idealresult = False
    print(result)
    assert result == idealresult, False