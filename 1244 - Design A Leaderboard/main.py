class Leaderboard(object):
    
    def __init__(self):
        self.__scorecollections__ = {}
        

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if not playerId in self.__scorecollections__:
            self.__scorecollections__[playerId] = score
        else :
            self.__scorecollections__[playerId] += score
        

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        sortedscorecollection = sorted(self.__scorecollections__.items(), key=lambda item: item[1], reverse=True )
        print(sortedscorecollection)
        result = 0
        for index in range(K):
            result += sortedscorecollection[index][1]
        return result
        

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        del self.__scorecollections__[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)