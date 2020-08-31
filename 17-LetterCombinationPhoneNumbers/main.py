class Solution(object):
    mattable = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
                '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
                '8':['t','u','v'], '9':['w','x','y','z']}
    def dfs(self, source, index, result, path):
        if index == len(source):
            if path != '':
                result.append(path)
            return
        for parts in self.mattable[source[index]]:
            self.dfs(source, index + 1, result, path + parts)
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        tmp = set(digits)
        if '1' in tmp:
            return
        result = []
        self.dfs(digits, 0, result, '')
        return result

if __name__ == '__main__':
    source = '2345'
    result = Solution().letterCombinations(source)
    print(result)
        
            