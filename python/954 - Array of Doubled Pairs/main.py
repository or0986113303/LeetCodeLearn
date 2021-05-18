import collections
class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # using the hash map to record all of occured eletment
        # and using the Counter method to caculate times
        # finally the judgement which is if there are two pairs 
        # and it's must following rule which x2 equal to 2 * x1 
        result = False
        if not A :
            result = True
        elif len(A) % 2 == 0 :
            SourceCollect = collections.Counter(A)
            print(SourceCollect)
            SortedSource = sorted(A, key=abs, reverse=False)
            print(SortedSource)
            for part in SortedSource:
                print(part)
                if SourceCollect[part] == 0:
                    continue
                if SourceCollect[part*2] == 0:
                    return False
                SourceCollect[part] -= 1
                SourceCollect[part*2] -= 1
            result = True
        else :
            result = False
        return result
        
if __name__ == "__main__":
    source = [4,-2,2,-4]
    idealresult = True
    result = Solution().canReorderDoubled(source)
    print(result)
    assert result == idealresult, False