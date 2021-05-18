class Solution(object):
    def windowsilde(self, source, capacity):
        targethash = {}
        headindex, tailindex = 0, 0
        maxdistance = float('-inf')
        while tailindex < capacity:
            if source[tailindex] not in targethash:
                targethash[source[tailindex]] = 1
            else:
                targethash[source[tailindex]] += 1

            maxdistance = max(maxdistance, tailindex - headindex)
            tailindex += 1
            while len(targethash) > 2:
                if targethash[source[headindex]] != 0:
                    targethash[source[headindex]] -= 1
                if targethash[source[headindex]] == 0:
                    del targethash[source[headindex]]
                headindex += 1
        # finally double check to maxmum length is needed change the greater one or not 
        return max(maxdistance, tailindex - headindex) 

    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        elif len(s) <= 2:
            return len(s)
        
        return self.windowsilde(s, len(s))
        
if __name__ == "__main__":
    source = "ccaabbb"
    idealresult = 5
    result = Solution().lengthOfLongestSubstringTwoDistinct(source)
    print(result)
    assert result == idealresult, False