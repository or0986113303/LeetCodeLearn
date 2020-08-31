class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        hashtable = {}
        result = {}
        
        for index, parts in enumerate(words):
            if not parts in hashtable:
                hashtable[parts] = [index]
            else :
                hashtable[parts].append(index)
        
        for position1 in hashtable[word1]:
            for position2 in hashtable[word2]:
                if not (word1, word2) in result :
                    if position1 != position2 :
                        result[(word1, word2)] = abs(position1 - position2)
                else :
                    if position1 != position2 :
                        result[(word1, word2)] = min(result[(word1, word2)], abs(position1 - position2))
        return result[(word1, word2)]
        
if __name__ == '__main__':
    words = ["a","a"]
    word1 = "a"
    word2 = "a"
    result = Solution().shortestWordDistance(words, word1, word2)
    print(result)