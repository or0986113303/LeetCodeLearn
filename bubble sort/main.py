class Solution(object):
    def bubblesort(self, source):
        if len(source) <= 1:
            return source
        for traversalindex in range(len(source)):
            for sortindex in range(1, len(source) - traversalindex, 1):
                if source[sortindex - 1] > source[sortindex]:
                    source[sortindex - 1], source[sortindex] = source[sortindex], source[sortindex - 1]
        return source


if __name__ == "__main__":
    source = [6,1,2,8,2,9,3,10]
    result = Solution().bubblesort(source)
    print(result)