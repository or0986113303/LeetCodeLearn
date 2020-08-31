class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        while len(arr) > k:
            if x - arr[0] <= arr[-1] - x:
                arr.pop()
            else:
                arr.pop(0)
        return arr
if __name__ == "__main__":
    source = [1,2,3,4,5]
    k = 4
    x = 3
    idealresult = [1,2,3,4]
    result = Solution().findClosestElements(source, k, x)
    print(result)
    assert result == idealresult, False