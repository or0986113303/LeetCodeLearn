class Solution(object):
    vowelsmap = ['a','i','e','u','o', 'A', 'I', 'E', 'U', 'O']
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s :
            return ''
        elif len(s) == 2:
            if s[0] in self.vowelsmap and s[1] in self.vowelsmap:
                result = s[::-1]
                return ''.join(result)
                
        result = []
        resultstr = ''
        for parts in s :
            result.append(parts)
        
        leftpointer, rightpointer = 0, len(s) - 1
        while leftpointer <= rightpointer:
            if s[leftpointer] in self.vowelsmap:
                if s[rightpointer] in self.vowelsmap:
                    result[leftpointer], result[rightpointer] = result[rightpointer], result[leftpointer]
                    leftpointer += 1
                    rightpointer -= 1
                else : 
                    rightpointer -= 1
            else :
                leftpointer += 1
                
        return ''.join(result)