class Solution(object):
    def caculatesumofcandy(self, forward, reverse):
        if len(forward) != len(reverse):
            return 0
        result = 0
        for index, part in enumerate(forward):
            result += max(part, reverse[index])
        return result
        
    def caculatecandysofeveryone(self, source, start, end, interval):
        result = [1] * len(source)
        if interval > 0 :
            for index in range(start, end, interval):
                if source[index] > source[index - 1]:
                    result[index] = result[index - 1] + 1
        else :
            for index in range(start, end, interval):
                if source[index] < source[index - 1]:
                    result[index - 1] = result[index] + 1
        return result

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        elif len(ratings) <= 1:
            return len(ratings)
        capacity = len(ratings)
        forward = self.caculatecandysofeveryone(ratings, 1, capacity, 1)
        reverse = self.caculatecandysofeveryone(ratings, capacity - 1, 0, -1)
        return self.caculatesumofcandy(forward, reverse)
        
if __name__ == "__main__":
    source = [1,2,2]
    idealresult = 4
    result = Solution().candy(source)
    print(result)
    assert result == idealresult