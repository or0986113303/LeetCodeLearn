class Sort:
    def mergeSort(self, alist):
        if len(alist) <= 1:
            return alist

        mid = len(alist) // 2
        left = self.mergeSort(alist[:mid])
        print("left = " + str(left))
        right = self.mergeSort(alist[mid:])
        print("right = " + str(right))
        return self.mergeSortedArray(left, right)

    def mergeSortedArray(self, A, B):
        sortedArray = []
        l = 0
        r = 0
        while l < len(A) and r < len(B):
            if A[l] < B[r]:
                sortedArray.append(A[l])
                l += 1
            else:
                sortedArray.append(B[r])
                r += 1
        sortedArray += A[l:]
        sortedArray += B[r:]

        return sortedArray





class Solution(object):
    def mergesort(self, source):
        if len(source) <= 1:
            return source
        middleindex = len(source) >> 1
        left = self.mergesort(source[:middleindex])
        print('left : ' + str(left))
        right = self.mergesort(source[middleindex:])
        print('right : ' + str(right))
        return self.merge(left, right)

    def merge(self, leftsource, rightsource):
        result = []
        leftindex, rightindex = 0, 0

        while leftindex < len(leftsource) and rightindex < len(rightsource):
            if leftsource[leftindex] < rightsource[rightindex]:
                result.append(leftsource[leftindex])
                leftindex += 1
            else :
                result.append(rightsource[rightindex])
                rightindex += 1
        result += leftsource[leftindex:]
        result += rightsource[rightindex:]
        return result

if __name__ == "__main__":
    unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
    #merge_sort = Sort()
    #print(merge_sort.mergeSort(unsortedArray))
    result = Solution().mergesort(unsortedArray)
    print(result)
