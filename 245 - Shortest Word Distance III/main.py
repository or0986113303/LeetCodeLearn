class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return 0
        wordshash = {}
        for index, part in enumerate(words):
            if part not in wordshash:
                wordshash[part] = [index]
            else:
                wordshash[part].append(index)
        
        minidistance = float('inf')
        
        if word1 in wordshash:
            for position1 in wordshash[word1]:
                if word2 in wordshash:
                    for position2 in wordshash[word2]:
                        if position1 != position2:
                            minidistance = min(minidistance, abs(position1 - position2))
        return minidistance
        
if __name__ == '__main__':
    words = ["a","a"]
    word1 = "a"
    word2 = "a"
    result = Solution().shortestWordDistance(words, word1, word2)
    print(result)