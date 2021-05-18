class Solution(object):
    def binarysearch(self, source, target):
        if not source :
            return -1
        
        leftindex, rightindex = 0, len(source) - 1

        while leftindex < rightindex:
            middle = (leftindex + rightindex) >> 1
            if source[middle] == target:
                leftindex = middle
                return leftindex
            elif source[middle] < target:
                leftindex = middle
            else :
                rightindex = middle
        
        if source[leftindex] == target :
            return leftindex
        if source[rightindex] == target :
            return rightindex
        return -1

if __name__ == "__main__":
    source = [1,2,3,4,5,6,7,8,9,10]
    target = 2
    result = Solution().binarysearch(source, target)
    print(result)
