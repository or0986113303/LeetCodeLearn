class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        # there are just 26 distinct of english letter and it can only map to the other letter one by one
        # if the count of collection of str1 or str2 is greater than 26, just return str1 compare with str2
        maphash = {}
        result = ''
        for index, part in enumerate(str1) :
            if part not in maphash :
                maphash[part] = str2[index]
            elif maphash[part] != str2[index]:
                return False
            result += maphash[part]
        print(result)
        print(str2)
        return str1 == str2 if len(set(str2)) == 26 else result == str2