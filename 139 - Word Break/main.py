class Solution(object):
    def dfs(self, source, target, startindex, result):
        if startindex == len(target):
            return
        sourcetmp = source
        tmptarget = target[startindex:]
        for _, parts in enumerate(tmptarget) :
            tmpresult = sourcetmp.split(parts)
            sourcetmp = ''
            for _, subparts in enumerate(tmpresult) :
                if subparts != '' :
                    sourcetmp += ',' + subparts
        resultstring = ''
        sourcetmp = sourcetmp.split(',')
        for parts in sourcetmp:
            resultstring += parts
        if resultstring == '':
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
    source = 'ccaccc'
    wordDict = ["cc","ac"]
    result = Solution().wordBreak(source, wordDict)
    print(result)