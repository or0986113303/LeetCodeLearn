class Solution(object):
    def isSubsequence(self, s, t):
        leftlength, rightlength = len(s), len(t)

        leftpointer = rightpointer = 0
        while leftpointer < leftlength and rightpointer < rightlength:
            # move both pointers or just the right pointer
            if s[leftpointer] == t[rightpointer]:
                leftpointer += 1
            rightpointer += 1

        return leftpointer == leftlength
        
if __name__ == "__main__":
    pass