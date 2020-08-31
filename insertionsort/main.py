class Solution(object):
    def insertionsort(self, source):
        for rightindex in range(1, len(source)): 
            target = source[rightindex] 
            leftindex = rightindex-1
            while leftindex >= 0 and source[leftindex] > target : 
                source[leftindex + 1] = source[leftindex] 
                leftindex -= 1
            source[leftindex + 1] = target 
        return source

if __name__ == "__main__":
    source = [1,6,2,9,3,10,4,5]
    idealresult = [1,2,3,4,5,6,9,10]
    result = Solution().insertionsort(source)
    print(result)
    assert result == idealresult