class Solution(object):
    def mergesort(self, source):
        if len(source) <= 1:
            return source
        middle = len(source) // 2
        leftpart = self.mergesort(source[:middle])
        rightpart = self.mergesort(source[middle:])
        return self.merge(leftpart, rightpart)
    def merge(self, leftpart, rightpart):
        result = []
        leftindex, rightindex = 0, 0
        while len(leftpart) > leftindex and len(rightpart) > rightindex:
            if leftpart[leftindex] > rightpart[rightindex] :
                result.append(rightpart[rightindex])
                rightindex += 1
            else : 
                result.append(leftpart[leftindex])
                leftindex += 1
        result += leftpart[leftindex:]
        result += rightpart[rightindex:]
        return result
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        elif len(nums) <= 1:
            return -1
        sortednums = self.mergesort(nums)
        #nums.sort()
        for index in range(1, len(sortednums), 1):
            if sortednums[index - 1] == sortednums[index]:
                return sortednums[index]

if __name__ == "__main__":
    source = [3,2,2,5,1]
    idealresult = 2
    result = Solution().findDuplicate(source)
    print(result)
    assert result == idealresult, False