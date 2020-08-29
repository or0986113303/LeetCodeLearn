class Solution(object):
    def peakIndexInMountainArray(self, A):
        left, right = 0, len(A) - 1
        while left < right:
            middle = (left + right) // 2
            if A[middle] < A[middle + 1]:
                left = middle + 1
            else:
                right = middle
        return left
        
if __name__ == "__main__":
    source = [1,2,2]
    idealresult = 1
    result = Solution().peakIndexInMountainArray(source)
    print(result)
    assert result == idealresult, False