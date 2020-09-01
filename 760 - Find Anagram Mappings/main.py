class Solution(object):
    def dfs(self, source, index, target, end, result):
        if index == end :
            return
        elif source[index] == target:
            result.append(index)
            return
        self.dfs(source, index + 1, target, end, result)
    
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        if not A or not B :
            return []
        elif len(A) != len(B):
            return []
        
        result = []
        for part in A :
            self.dfs(B, 0, part, len(B), result)
        return result
        
if __name__ == "__main__":
    A = [12,28,46,32,50]
    B = [50,12,32,46,28]
    idealresult = [1,4,3,2,0]
    result = Solution().anagramMappings(A,B)
    print(result)
    assert result==idealresult, False