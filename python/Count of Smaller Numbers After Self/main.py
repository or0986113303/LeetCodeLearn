class Solution(object):
    def dfs(self, source, target, searchindex, targetindex, result):
        if not source :
            return
        elif searchindex > len(source) - 1 :
            return
        if target > source[searchindex] :
            result[targetindex] += 1
        self.dfs(source, target, searchindex + 1, targetindex, result)

    def test(self, source):
        result = [0]*len(source)
        for index, part in enumerate(source):
            self.dfs(source, part, index + 1, index, result)
        return result

if __name__ == "__main__":
    nums = [5,2,6,1]
    idealresult = [2,1,1,0]
    result = Solution().test(nums)
    print(result)
    assert result == idealresult, False
