class WordDistance(object):
    
    def __init__(self, words):
        self.__source__ = words
        self.__hashatable__ = {}
        self.__result__ = {}
        self.__hashatable__ = self.__createhashfromsource__(words)
        
    def __createhashfromsource__(self, source):
        tmphash = {}
        for index, parts in enumerate(source):
            if not parts in tmphash:
                tmphash[parts] = [index]
            else:
                tmphash[parts].append(index)
        return tmphash
        
    def shortest(self, word1, word2):
        for position1 in self.__hashatable__[word1]:
            for position2 in self.__hashatable__[word2]:
                if not (word1, word2) in self.__result__:
                    self.__result__[(word1, word2)] = abs(position1 - position2)
                else :
                    self.__result__[(word1, word2)] = min(self.__result__[(word1, word2)], abs(position1 - position2))
        return self.__result__[(word1, word2)]

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