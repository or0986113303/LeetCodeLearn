class Solution(object):
    def sumofsqrt(self, source):
        return source[0] ** 2 + source[1] ** 2
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        hashtable = {}
        result = []
        count = 0
        for parts in points:
            hashtable[(parts[0], parts[1])] = self.sumofsqrt(parts)
        counthashsorted = sorted(hashtable.items(), key=lambda item: item[1], reverse=False)
        for _, key in enumerate(counthashsorted):
            if count < K :
                result.append(key[0])
                count += 1
        return result

if __name__ == "__main__":
    source = [[3,3],[5,-1],[-2,4]]
    k = 2
    result = Solution().kClosest(source, k)
    idealresult = [(3,3),(-2,4)]
    print(result)
    assert result == idealresult, False