class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2 :
            return 0.0
        sourcetmp = nums1 + nums2
        sourcetmp.sort()
        result = 0
        if len(sourcetmp) % 2 == 0:
            result = (float(sourcetmp[len(sourcetmp) // 2]) + float(sourcetmp[len(sourcetmp) // 2 - 1])) / 2
        else :
            result = float(sourcetmp[((len(sourcetmp) - 1) // 2 )])
        return result

if __name__ == '__main__' :
    source1 = [3,1,4,7]
    source2 = [9,2,8]
    result = Solution().findMedianSortedArrays(source1, source2)
    print(result)