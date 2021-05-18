class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        resulthash = {}
        for parts in emails:
            localname, domainname = parts.split('@')
            if '+' in localname:
                localname = localname[:localname.index('+')]
            mail = localname.replace('.', '') + '@' + domainname
            if mail not in resulthash:
                resulthash[mail] = 1
            else :
                resulthash[mail] += 1
        return len(resulthash)

if __name__ == "__main__":
    source = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
    idealresult = 2
    result = Solution().numUniqueEmails(source)
    print(result)
    assert result == idealresult, False