class Solution(object):
    def dfs(self, source, target, startindex, result):
        if startindex == len(target):
            return
        sourcetmp = source
        tmptarget = target[startindex:]
        for index, parts in enumerate(tmptarget) :
            tmpresult = sourcetmp.split(parts)
            sourcetmp = ''
            for _, subparts in enumerate(tmpresult) :
                if subparts != '' :
                    sourcetmp += subparts
        if sourcetmp == '':
            result.append(True)
        else : 
            result.append(False)
        self.dfs(source, target, startindex + 1, result)

    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return False
        result = []
        self.dfs(s, wordDict, 0, result)
        return True in result
            


if __name__ == '__main__':
    source = 'catsandog'
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    result = Solution().wordBreak(source, wordDict)
    print(result)