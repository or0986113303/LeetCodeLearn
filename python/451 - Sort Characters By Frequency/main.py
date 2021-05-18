class Solution(object):
    def __mergesort__(self, source):
        if len(source) <= 1:
            return source
        middle = len(source) >> 1
        leftpart = self.__mergesort__(source[:middle])
        rightpart = self.__mergesort__(source[middle:])
        return self.__merge__(leftpart, rightpart)
        
    def __merge__(self, leftpart, rightpart):
        result = []
        leftindex = 0
        rightindex = 0
        while len(leftpart) > leftindex and len(rightpart) > rightindex:
            if leftpart[leftindex][0] > rightpart[rightindex][0]:
                result.append(rightpart[rightindex])
                rightindex += 1
            else :
                result.append(leftpart[leftindex])
                leftindex += 1
        result += leftpart[:leftindex]
        result += rightpart[:rightindex]
        return result
        
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counthash = {}
        for parts in s:
            if not parts.encode('utf-8') in counthash:
                counthash[parts.encode('utf-8')] = 1
            else :
                counthash[parts.encode('utf-8')] += 1
        #counthashsorted = self.__mergesort__(counthash)
        #counthashsorted = {k: v for k, v in sorted(counthash.items(), key=lambda item: item[1])}
        counthashsorted = sorted(counthash.items(), key=lambda item: item[1], reverse=True)
        result = ''
        for part in counthashsorted:
            for _ in range(0, part[1],1):
                result += part[0]
        print(result)
        return result
        
        