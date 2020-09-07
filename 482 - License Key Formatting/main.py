class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not S :
            return ''
        
        result = []
        sourcestringtmp = "".join(S.split("-")).upper()
        capacity = len(sourcestringtmp)
        # to determine the capacity of remaining group can be divided by K
        # otherwise set the remainder of capacity of string to the first group
        if capacity % K != 0:
            result.append(sourcestringtmp[: capacity % K])
        for index in range(capacity % K, capacity, K):
            result.append(sourcestringtmp[index : index + K])
        return "-".join(result)
        
        
if __name__ == "__main__":
    
    source = "2-4A0r7-4k"
    K = 4
    result = Solution().licenseKeyFormatting(source, K)
    print(result)