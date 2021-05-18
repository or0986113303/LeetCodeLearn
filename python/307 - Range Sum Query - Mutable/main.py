class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__source__ = nums
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.__source__[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.__source__[i:j + 1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)