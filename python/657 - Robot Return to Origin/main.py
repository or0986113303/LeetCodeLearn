class Solution(object):
    maptable = {'L':1, 'R':-1, 'U':10, 'D':-10}
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if not moves:
            return True
        elif len(moves) == 0:
            return True
        elif len(moves) % 3 == 0:
            return False
        result = 0
        for parts in moves:
            result += self.maptable[parts]
        
        return result == 0