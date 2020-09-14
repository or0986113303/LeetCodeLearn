class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers is None:
            return [-1, -1]
        elif target is None:
            return [-1, -1]
        
        leftindex, rightindex = 0, len(numbers) - 1
        
        while rightindex >= leftindex:
            middle = numbers[rightindex] + numbers[leftindex]
            if middle == target:
                return [leftindex + 1, rightindex + 1] if rightindex > leftindex else [rightindex + 1, leftindex + 1]
            elif middle > target:
                rightindex -= 1
            else :
                leftindex += 1
        
        return [-1, -1]