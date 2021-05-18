class WordDistance(object):
    
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.__wordshash__ = {}
        for index, part in enumerate(words):
            if part not in self.__wordshash__:
                self.__wordshash__[part] = [index]
            else :
                self.__wordshash__[part].append(index)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return 0
        minidistance = float('inf')
        if word1 in self.__wordshash__:
            for position1 in self.__wordshash__[word1]:
                if word2 in self.__wordshash__:
                    for position2 in self.__wordshash__[word2]:
                        if position1 != position2:
                            minidistance = min(minidistance, abs(position1 - position2))
        return minidistance

if __name__ == "__main__":
    words = ["a","a"]
    word1 = 'a'
    word2 = 'a'
    tmp = WordDistance(words=words)
    result = tmp.shortest(word1, word2)
    print(result)
    word1 = 'b'
    word2 = 'a'
    result = tmp.shortest(word1, word2)
    print(result)