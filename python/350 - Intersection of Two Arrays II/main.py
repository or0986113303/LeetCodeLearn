import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        source = collections.Counter(nums1) if collections.Counter(nums1) > collections.Counter(nums2) else collections.Counter(nums2)
        target = collections.Counter(nums2) if source == collections.Counter(nums1) else collections.Counter(nums1)
        result = []
        
        for part, key in enumerate(target):
            if key in source:
                for _ in range(0, min(target[key], source[key]), 1):
                    result.append(key)
        print(result)
        return result
        
        