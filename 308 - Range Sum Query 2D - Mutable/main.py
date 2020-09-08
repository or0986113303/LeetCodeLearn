class NumMatrix(object):
    
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.__source__ = matrix
        

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        self.__source__[row][col] = val
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sumtmp = 0
        for index in range(row1, row2 + 1, 1):
            sumtmp += sum(self.__source__[index][col1:col2 + 1])
        return sumtmp


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)