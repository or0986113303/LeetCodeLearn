import collections
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        source = nums1
        target = nums2
        workindex = 0
        for index, part in enumerate(source):
            print(workindex)
            if part == 0:
                if workindex != len(target):
                    source[index] = target[workindex]
                    workindex +=1
        source.sort()
        
if __name__ == "__main__":
    source1 = [1,2,3,4,0,0,0]
    m = len(source1)
    source2 = [7,5,2]
    n = len(source2)
    Solution().merge(source1, m, source2, n)
    print(source1)