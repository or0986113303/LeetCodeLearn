class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        xlength = len(matrix)
        ylength = len(matrix[0])
        result = matrix
        for xindex in range(0, xlength//2 + xlength%2, 1):
            for yindex in range(0, ylength//2, 1):
                # buffer left buttom value
                tmp = result[ylength - 1 - yindex][xindex] 
                # rotate right buttom value to left buttom
                result[ylength - 1 - yindex][xindex] = result[xlength - 1 - xindex][ylength - yindex - 1] 
                # rotate right top to right buttom
                result[xlength - 1 - xindex][ylength - yindex - 1] = result[yindex][xlength - 1 - xindex]
                # rotate left top to right top
                result[yindex][xlength - 1 - xindex] = result[xindex][yindex]
                # rotate left buttom to left top
                result[xindex][yindex] = tmp
        