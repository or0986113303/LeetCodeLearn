class Solution(object):
    def windowslide(self, source, capacity, distinctarget):
        headindex, tailindex = 0, 0
        substringhash = {}
        maxlength = float('-inf')
        while tailindex < capacity:
            print(source[tailindex])
            if source[tailindex] not in substringhash:
                substringhash[source[tailindex]] = 1
            else :
                substringhash[source[tailindex]] += 1
            while len(substringhash) > distinctarget:
                if substringhash[source[headindex]] != 0 :
                    substringhash[source[headindex]] -= 1
                    if substringhash[source[headindex]] == 0 :
                        del substringhash[source[headindex]]
                headindex += 1
            maxlength = max(maxlength, tailindex - headindex + 1)
            tailindex += 1
        return maxlength
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s :
            return 0
        
        capacity = len(s)
        
        return self.windowslide(s, capacity, k)

if __name__ == "__main__":
    source = 'eceba'
    k = 2
    idealresult = 3
    result = Solution().lengthOfLongestSubstringKDistinct(source, k)
    print(result)
    assert result == idealresult, False