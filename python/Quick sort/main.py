class Solution(object):
    def partion(self, source, leftindex, rightindex):
        leftsearchindex = leftindex-1 
        pivot = source[rightindex]
    
        for rightsearchindex in range(leftindex , rightindex): 
            if   source[rightsearchindex] < pivot: 
                leftsearchindex += 1 
                source[leftsearchindex],source[rightsearchindex] = source[rightsearchindex],source[leftsearchindex] 
    
        source[leftsearchindex+1],source[rightindex] = source[rightindex],source[leftsearchindex+1] 
        return leftsearchindex+1 
    def quicksort(self, source, leftindex, rightindex):
        if not source :
            return 
        elif len(source) <= 1:
            return 
        if leftindex < rightindex :
            middle = self.partion(source, leftindex, rightindex)
            self.quicksort(source, leftindex, middle - 1)
            self.quicksort(source, middle + 1, rightindex)


if __name__ == "__main__":
    source = [20,1,3,6,19,64,4,7,9,33]
    idealresult = [1,3,4,6,7,9,19,20,33,64]
    result = []
    leftindex, rightindex = 0 , len(source) - 1
    Solution().quicksort(source ,leftindex, rightindex)
    print(source)
    assert source == idealresult, True