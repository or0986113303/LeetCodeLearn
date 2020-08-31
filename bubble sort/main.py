class Solution(object):
    def BubbleSort(self, source):
        if not source:
            return []
        for index in range(1, len(source), 1):
            for groupindex in range(1, len(source) - index, 1):
                if source[groupindex - 1] > source[groupindex]:
                    source[groupindex - 1], source[groupindex] = source[groupindex], source[groupindex - 1]
        return source

if __name__ == '__main__':

    source = [64, 34, 25, 12, 22, 11, 90, 1, 23, 2, 4]
    result = Solution().BubbleSort(source)
    print(source)