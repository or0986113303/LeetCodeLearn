class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.source = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        result = 0
        if len(self.source) == len(vec.source):
            for index in range(len(self.source)):
                result += self.source[index] * vec.source[index]
            return result
        else:
            return -1
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)