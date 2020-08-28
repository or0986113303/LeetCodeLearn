class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        length1 = len(nums1)
        length2 = len(nums2)
        
        if length1 > length2:
            target = nums2
            source = nums1
        else :
            target = nums1
            source = nums2
        result = []
        for parts in target:
            if parts in source:
                source.remove(parts)
                result.append(parts)
        return result
        