class Solution(object):
    def dfs(self, source, target, startindex, result, resultcollection):
        # inplement by in-place to save the space complexity to O(1)
        if target < 0:
            return
        elif target == 0:
            # assume the target equal to zero reprecenting find all numbers of the sum equal to target
            result.append(resultcollection)

        for searchindex in range(startindex, len(source), 1):
            if source[searchindex] > target:
                return
            elif searchindex > startindex and source[searchindex] == source[searchindex-1]:
                # avoid the duplicate result
                continue
            self.dfs(source, target - source[searchindex], searchindex + 1, result, resultcollection + [source[searchindex]])

    def combinationSum(self, candidates, target):
        # corner case
        if not candidates:
            return
        # the source must be sorted
        candidates.sort()
        # operation variable
        result = []
        self.dfs(candidates, target, 0, result, [])
        return result
        
if __name__ == '__main__' :
    source = [10,1,2,7,6,1,5]
    target = 8
    result = Solution().combinationSum(source, target)
    print(result)