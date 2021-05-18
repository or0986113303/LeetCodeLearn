class Solution(object):
    def findContestMatch(self, n):
        team = map(str, range(1, n+1))
        print(team)
        while n > 1:
            for i in range(n // 2):
                team[i] = "({},{})".format(team[i], team.pop())
                print(team[i])
            n //= 2

        return team[0]
        