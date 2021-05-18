import math
class Solution(object):
    def jumpsearch(self, source, target):
        if not source :
            return -1
        step = int(math.sqrt(len(source)))
        prev = 0
        length = len(source)
        while source[min(prev, length)] < target:
            prev += step
            if prev >= length:
                return -1
        subindex = 0
        while source[prev - subindex] != target:
            subindex += 1
            if subindex == step:
                return -1
        return prev - subindex

if __name__ == "__main__":
    source = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    target = 21
    idealresult = 13
    result = Solution().jumpsearch(source, target)
    print(result)
    assert result == 13, False