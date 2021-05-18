import collections
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        source = collections.Counter(nums1) if len(collections.Counter(nums1)) > len(collections.Counter(nums2)) else collections.Counter(nums2)
        target = collections.Counter(nums2) if source == collections.Counter(nums1) else collections.Counter(nums1)
        
        result = []
        for part in target.keys():
            if part in source:
                result.append(part)
        print(result)
        return result