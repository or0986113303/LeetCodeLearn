class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        elif not s and not t:
            return True
        
        maphash = {}
        for index, part in enumerate(s):
            if part not in maphash:
                maphash[part] = t[index]
            elif maphash[part] != t[index]: 
                return False
        return len(maphash.values()) == len(set(maphash.values()))
                        
if __name__ == "__main__":
    s = 'aa'
    t = 'ab'
    idealresult = False
    result = Solution().isIsomorphic(s, t)
    print(result)
    assert result == idealresult, False