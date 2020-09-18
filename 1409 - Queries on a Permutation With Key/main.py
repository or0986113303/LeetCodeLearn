class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        mappingtable = [index for index in range(1,m + 1,1)]
        result = []
        for x in queries:
            temp = mappingtable.index(x)
            num = mappingtable[temp]
            result.append(temp)
            mappingtable.remove(mappingtable[temp])
            mappingtable.insert(0, num)
        return result
            