class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sourcestack = []
        targetstack = []
        for part in S :
            if part == '#' :
                if len(sourcestack) > 0 :
                    sourcestack = sourcestack[:-1]
            else : 
                sourcestack.append(part)
        for part in T :
            if part == '#' :
                if len(targetstack) > 0 :
                    targetstack = targetstack[:-1]
            else : 
                targetstack.append(part)
        return sourcestack == targetstack

if __name__ == "__main__":
    S = "y#fo##f"
    T = "y#f#o##f"
    idealresult = True
    result = Solution().backspaceCompare(S,T)
    print(result)
    assert result == idealresult, False