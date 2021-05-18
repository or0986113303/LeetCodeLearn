class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        index = float('-inf')
        capacity = len(seats)
        result = [0] * capacity
        for i in range(capacity):
            if seats[i] == 1:
                index = i
            else:
                result[i] = abs(i - index)
        index = float('-inf')
        for i in range(capacity - 1, -1, -1):
            if seats[i] == 1:
                index = i
            else:
                result[i] = min(abs(i - index), result[i])
        return max(result)
        
if __name__ == "__main__":
    source = [1,0,0,0,1,0,1]
    idealresult = 2
    result = Solution().maxDistToClosest(source)
    print(result)
    assert result == idealresult