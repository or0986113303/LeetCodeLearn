class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        hashtable = {}
        result = {}
        for index, parts in enumerate(words):
            if not parts in hashtable :
                hashtable[parts] = [index]
            else :
                hashtable[parts].append(index)
        
        #word1position for word1position in hashtable[word1] for word2position in hashtable[word2]
        for word1position in hashtable[word1] :
            for word2position in hashtable[word2]  :
                if not (word1,word2) in result:
                    result[(word1,word2)] = abs(word1position - word2position)    
                else :
                    result[(word1,word2)].update(min(abs(word1position - word2position), result[(word1,word2)])) 
            #print(word1position)
        return result[(word1, word2)]

if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = 'coding'
    word2 = 'practice'

    result = Solution().shortestDistance(words, word1, word2)
    print(result)