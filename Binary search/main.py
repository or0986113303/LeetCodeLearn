class Solution(object):
    def binarysearch(self, source, target):
        result = -1
        leftindex, rightindex = 0, len(source) - 1

        while leftindex < rightindex:
            middle = (leftindex + rightindex) >> 1
            if source[middle] == target:
                result = middle
                return result
            elif source[middle] < target:
                leftindex = middle
            elif source[middle] > target:
                rightindex = middle

        return result

if __name__ == "__main__":
    source = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,90,20,45,67]
    target = 2
    result = Solution().binarysearch(source, target)
    print(result)